<script setup>
import Loader from '../components/Loader.vue';
import Listing from '../components/Listing.vue';
//res.header("Access-Control-Allow-Origin", "*");
</script>

<script>
export default {
    props: [
        'query',
        'lat',
        'long'
    ],
    data() {
        return {
            locations: [],
            loading: true,
        }
    },
    created() {
        this.$watch(
            () => this.$route.params,
            () => {
                this.loading = true
                this.hydrate()
                console.log(this.locations)
            },
            { immediate: true }
        )
    },
    methods: {
        hydrate() {
            const url = new URL('http://127.0.0.1:5000/api/costco')
            if (this.query) {
                url.search = new URLSearchParams({q: this.query})
            }
            else {
                url.search = new URLSearchParams({lat: this.lat, long: this.long})
            }
            // console.log(url)
            fetch(url)
                .then(res => res.json())
                .then(data => {
                    this.locations = data.locations
                    this.loading = false
                })
        }
    }
}
</script>


<template>
    <Loader v-if="loading"></Loader>
    <div class="search-results" v-else>
        <h1>Fuel Stations</h1>
        <p>Star your favourite locations for easier access in the future.</p>
        <p class="query" v-if="query">
            Map queries are processed using data from the 
            <!-- a href="https://www.openstreetmap.org/copyright">OpenStreetMap Foundation licensed under the Open Database License</a--></p>
        <Listing :locations="locations"></Listing>
    </div>
</template>


<style scoped>
    h1 {
        margin-bottom: 0;
    }

    p {
        margin-top: 0;
    }

    p.query{
        font-family: 'Inconsolata', monospace;
        font-weight: 300;
    }

    p.query > a {
        text-decoration: underline;
        text-decoration-style: dashed;
        text-decoration-thickness: 1.5px;
        color: black;
    }
</style>