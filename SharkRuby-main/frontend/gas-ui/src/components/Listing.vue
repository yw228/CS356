<script setup>
import Costco from './Costco.vue';
</script>

<script>
export default {
    props: ['locations']
}
</script>


<template>
    <div class="results">
        <Costco v-for="location in locations" :costco="location" v-show="location.gas.available"></Costco>
    </div>
    <p class="disclaimer">
        Price data is pulled from fuel Costco's servers. Purchases will be made at the prices posted at the point of sale.
    </p>
</template>


<style scoped>
    @media only screen and (min-width: 720px) {
        .results {
            grid-template-columns: 1fr 1fr;
        }
    }

    @media only screen and (min-width: 1000px) {
        .results {
            grid-template-columns: 1fr 1fr 1fr;
        }
    }

    span.strike {
        text-decoration: line-through;
    }

    p {
        margin-top: 0;
    }

    p.disclaimer{
        font-family: 'Inconsolata', monospace;
        font-weight: 300;
    }

    .results {
        display: grid;
        gap: 10px 20px;
    }
</style>