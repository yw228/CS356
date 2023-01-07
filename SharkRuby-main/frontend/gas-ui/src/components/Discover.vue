<script>
export default {
    data() {
        return {
            searching: false,
            searchQuery: '',
            gpsText: 'GPS'
        }
    },
    methods: {
        search() {
            if (!this.searching && this.searchQuery == '') {
                this.searching = true
                this.$nextTick(() => this.searchFocus())
                return
            }
            else {
                if (this.searchQuery.length > 0) {
                    console.log('Searching for: ', this.searchQuery)
                    this.$router.push({
                        name: 'query',
                        params: {
                            query: this.searchQuery
                        }
                    })
                    
                }
                else {
                    this.searching = true
                    this.$nextTick(() => this.searchFocus())
                    return
                }
            }
        },
        searchBlur() {
            // this.searching = false
            // this.searchQuery = ''
        },
        searchFocus() {
            document.getElementById('badchrome').focus()
            // document.getElementById('badchrome').scrollIntoView()
        },
        gps() {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    console.log('Searching at: ', position.coords.latitude, position.coords.longitude)
                    this.$router.push({
                        name: 'gps',
                        params: {
                            lat: position.coords.latitude,
                            long: position.coords.longitude
                        } 
                    })
                },
                (err) => {
                    this.gpsText = 'GPS Error'
                    this.search()
                }
            )
        }
    }
}
</script>


<template>
    <div class="discover">
        <h1>Find Stations</h1>
        <div class="actions">
            <div class="option button" @click="gps">
                <img class="icon-option" src="@/assets/gps.svg" />
                <div class="label">
                    {{gpsText}}
                </div>
                <img class="icon-option arrow" src="@/assets/right.svg" />
            </div>
            <div class="option button" @click="search">
                <img class="icon-option" src="@/assets/map.svg" />
                <div class="label" v-show="!searching">
                    Search
                </div>
                <form v-show="searching" @submit.prevent="search" class="search-form" autocomplete="off">
                    <input type="text" id="badchrome" v-model="searchQuery" class="search-text" placeholder="City, ZIP Code, etc ..." @blur="searchBlur" autocomplete="postal-code" name="badchrome">
                </form>
                <img class="icon-option arrow" src="@/assets/right.svg" />
            </div>
            <div class="bad-chrome option" v-show="searching"></div>
        </div>
    </div>
</template>


<style>
    .option{
        display: grid;
        grid-template-columns: 35px 1fr auto;
        gap: 10px;
        align-items: center;
        justify-items: center;
        align-content: center;
        justify-content: center;
        font-family: 'Inconsolata', monospace;
        font-weight: 700;
        font-size: 30px;
    }

    .option.button{
        border: 2px solid black;
        border-radius: 15px;
        padding: 10px;
        margin: 10px 0;
        cursor: pointer;
        user-select: none;
        -webkit-user-select: none;
        -webkit-touch-callout: none;
    }

    .icon-option{
        height: 35px;
    }

    .icon-option.arrow{
        width: 15px;
    }

    .discover > h1 {
        margin-bottom: 0;
    }

    .search-form {
        width: 100%;
    }

    .search-text {
        box-sizing: border-box;
        border: 0;
        font-family: 'Inconsolata', monospace;
        font-weight: 500;
        font-size: 24px;
        outline: none;
        width: 100%;
        height: 100%;
        padding: 0;
    }

    .search-text::placeholder{
        color: grey;
        font-weight: 700

    }

</style>