<script>
export default {
    props: ['price', 'type'],
    computed: {
        baseCost() {
            return this.price.slice(0, -1)
        },
        scam() {
            return this.price.slice(-1)
        },
        red() {
            return this.type === 'premium'
        },
        blue() {
            return this.type === 'regular'
        },
        green() {
            return this.type === 'diesel'
        }
    }
}
</script>


<template>
    <div class="fuel" :class="{red: red, green: green, blue:blue}">
        <div class="price">${{baseCost}}<span class="scam">{{scam}}</span></div>
        <div class="type">{{type}}</div>
    </div>
</template>


<style scoped>
    .fuel {
        font-family: 'Inconsolata', monospace;
        text-align: center;
        width: 100%;
        color: white;
        padding: 2px;
        border-radius: 5px;
    }

    .red {
        background-color: var(--red);
    }

    .green {
        background-color: var(--green);
    }

    .blue {
        background-color: var(--blue);
    }
    
    .price {
        font-weight: 800;
        font-size: 25px
    }

    .scam {
        vertical-align: text-top;
        font-size: 15.5px;
    }

    .type {
        font-weight: 400;
        text-transform: uppercase;
    }
</style>