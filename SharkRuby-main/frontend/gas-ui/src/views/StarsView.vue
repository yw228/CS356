<script setup>
import Loader from '../components/Loader.vue';
import Listing from '../components/Listing.vue';

import { get } from 'idb-keyval';
</script>

<script>
export default {
    data() {
        return {
            locations: [],
            loading: true,
        }
    },
    created() {
        this.hydrate()
    },
    methods: {
        hydrate() {
            //res.header("Access-Control-Allow-Origin", "*");
            const url = new URL('http://127.0.0.1:5000/api/costco')
            get('stars').then(stars => {
                if (Array.isArray(stars) && stars.length > 0)
                {
                    url.search = new URLSearchParams({ids: stars})
                    fetch(url)
                        .then(res => res.json())
                        .then(data => {
                            this.locations = data.locations
                            this.loading = false
                        })
                }
                else {
                    this.loading = false
                }
            })
            
        },
        search() {
            this.$router.push({name: 'search'})
        }
    }
}
</script>


<template>
    <Loader v-if="loading"></Loader>
    <div v-else>
        <h1>Starred Stations</h1>
        
        <Listing :locations="locations" v-if="locations.length > 0"></Listing>
        <p v-else class="center">No starred stations, yet, <span class="anchor" @click="search">go find some</span>...</p>
    </div>
</template>


<style scoped>
    h1 {
        margin-bottom: 0;
    }

    p {
        margin-top: 0;
    }

    p.center {
        text-align: center;
    }

    span.anchor {
        text-decoration: underline;
        text-decoration-style: dashed;
        text-decoration-thickness: 1.5px;
        cursor: pointer;
    }

</style>