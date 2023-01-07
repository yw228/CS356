<script setup>
import Welcome from '../components/Welcome.vue';
import Discover from '../components/Discover.vue';

import { get } from 'idb-keyval';
</script>

<script>
export default {
    created() {

        get('stars').then(stars => {
            if (Array.isArray(stars) && stars.length > 0)
            {
                this.$router.push({name: 'stars'})
            }
            else {
                // Show New User Home
            }
        })

        document.getElementById('app').classList.add('homev')
        document.getElementsByTagName('html')[0].classList.add('homev')
        document.getElementsByTagName('body')[0].classList.add('homev')
        document.getElementById('navbar').classList.add('hidden')
        document.getElementById('buffer').classList.add('hidden')
    },
    unmounted() {
        document.getElementById('app').classList.remove('homev')
        document.getElementsByTagName('html')[0].classList.remove('homev')
        document.getElementsByTagName('body')[0].classList.remove('homev')
        document.getElementById('navbar').classList.remove('hidden')
        document.getElementById('buffer').classList.remove('hidden')
    }
}
</script>

<template>
    <div class="home">
        <Welcome></Welcome>
        <Discover></Discover>
    </div>
  
</template>

<style>
    @media only screen and (min-width: 720px) {
        .home {
            display: grid;
            grid-template-columns: 1fr 1fr;
            align-items: center;
            align-content: center;
            justify-content: center;
        }

        #app.homev {
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 100%;
        }

        body.homev, html.homev {
            height: 100%;
            margin: 0 auto;
        }

        p {
            text-align: left;
        }

        .bad-chrome{
            display: none;
        }
        
    }

    .bad-chrome{
        height: 35px;
    }
</style>
