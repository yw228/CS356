import httpx

costco_headers = {
    'authority': 'www.costco.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.costco.com/warehouse-locations?langId=-1&storeId=10301&catalogId=10701',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

nominatim_headers = {
    'user-agent': 'rubysharkgas/0.0.0'
}

def _query_costco_api_by_gps(lat, long):
    with httpx.Client(headers=costco_headers) as client:
        base = client.get('https://www.costco.com/warehouse-locations')
        payload = client.get(f'https://www.costco.com/AjaxWarehouseBrowseLookupView?langId=-1&storeId=10301&numOfWarehouses=50&hasGas=false&hasTires=false&hasFood=false&hasHearing=false&hasPharmacy=false&hasOptical=false&hasBusiness=false&hasPhotoCenter=&tiresCheckout=0&isTransferWarehouse=false&populateWarehouseDetails=true&warehousePickupCheckout=false&latitude={lat}&longitude={long}&countryCode=US')
        data = payload.json()[1:]
        return data

def _query_costco_api_by_warehouse(warehouse_id):
    with httpx.Client(headers=costco_headers) as client:
        base = client.get('https://www.costco.com/warehouse-locations')
        payload = client.get(f'https://www.costco.com/AjaxWarehouseBrowseLookupView?langId=-1&storeId=10301&numOfWarehouses=10&hasGas=&hasTires=&hasFood=&hasHearing=&hasPharmacy=&hasOptical=&hasBusiness=&hasPhotoCenter=&tiresCheckout=0&isTransferWarehouse=false&populateWarehouseDetails=true&warehousePickupCheckout=false&warehouseNumber={warehouse_id}&countryCode=')
        data = payload.json()
        if len(data) > 0:
            return data[1]
        else:
            return False

def _query_costco_api_by_warehouses(warehouse_ids):
    with httpx.Client(headers=costco_headers) as client:
        base = client.get('https://www.costco.com/warehouse-locations')
        ret = []
        for wid in warehouse_ids:
            payload = client.get(f'https://www.costco.com/AjaxWarehouseBrowseLookupView?langId=-1&storeId=10301&numOfWarehouses=10&hasGas=&hasTires=&hasFood=&hasHearing=&hasPharmacy=&hasOptical=&hasBusiness=&hasPhotoCenter=&tiresCheckout=0&isTransferWarehouse=false&populateWarehouseDetails=true&warehousePickupCheckout=false&warehouseNumber={wid}&countryCode=')
            data = payload.json()
            if len(data) > 0:
                ret.append(data[1])
    return ret

def _process_costco_entry(location):
    return {
        'id': location['stlocID'],
        'name': location['locationName'],
        'address': location['address1'].title(),
        'city': location['city'].title(),
        'state': location['state'],
        'zip': location['zipCode'],
        'gas': {
            'available': location['hasGasDepartment'],
            'regular': location.get('gasPrices', {}).get('regular'),
            'premium': location.get('gasPrices', {}).get('premium'),
            'diesel': location.get('gasPrices', {}).get('diesel'),
        }
    }

def _get_lat_long_from_query(query: str):
    geocode = httpx.get(f'https://nominatim.openstreetmap.org/search?q={query}&format=jsonv2', headers=nominatim_headers).json()
    return {
        'lat': geocode[0]['lat'],
        'long': geocode[0]['lon'],
    }

def get_costcos_from_gps(lat, long):
    costcos = _query_costco_api_by_gps(lat, long)
    ret = []
    for costco in costcos:
        ret.append(_process_costco_entry(costco))
    return ret

def get_costcos_from_query(query):
    gps = _get_lat_long_from_query(query)
    return get_costcos_from_gps(gps['lat'], gps['long'])

def get_costco_from_id(warehouse_id):
    return _process_costco_entry(_query_costco_api_by_warehouse(warehouse_id))

def get_costcos_from_ids(warehouse_ids):
    costcos = _query_costco_api_by_warehouses(warehouse_ids)
    ret = []
    for costco in costcos:
        ret.append(_process_costco_entry(costco))
    return ret

if __name__ == '__main__':
    gps = _get_lat_long_from_query('fullerton')
    locations = _query_costco_api_by_gps(gps['lat'], gps['long'])
    print(_process_costco_entry(locations[0]))