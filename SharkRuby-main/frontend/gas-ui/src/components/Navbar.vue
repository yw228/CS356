<script>
export default {
    methods: {
        search() {
            this.$router.push({name: 'search'})
        },
        stars() {
            this.$router.push({name: 'stars'})
        },
        home() {
            this.$router.push({name: 'home'})
        }
    }
}
</script>

<template>
    <div class="navbar" id="navbar">
        <img @click="home" src="@/assets/gas.svg" class="logo" />
        <div></div>
        <div class="wordmark"><div class="selective">Shark Ruby <span class="blue">Gas</span></div></div>
        <div></div>
        <button @click="search"><img src="@/assets/magglass.svg"/></button>
        <button @click="stars"><img src="@/assets/star.svg"/></button>
    </div>
    <div id="buffer"></div>
</template>

<style scoped>
    .navbar {
        display: grid;
        grid-template-columns: auto 1fr auto 1fr auto auto;
        align-items: center;
        justify-items: start;
        align-content: center;
        gap: 5px;
        position: fixed;
        top: 0px;
        left: 0px;
        right: 0px;
        padding: 5px 10px;
        background-color: var(--grey);
        opacity: 1;
        transition: opacity 0.5s;
        z-index: 100;
    }

    #buffer {
        height: 50px;
    }

    .wordmark{
        color: var(--red);
        font-family: 'Fugaz One', cursive;
        text-transform: uppercase;
        font-size: 32px;
    }

    span.blue {
        color: var(--blue);
    }

    img.logo {
        height: 60px;
        cursor: pointer;
    }

    button > img {
        height: 25px;
    }

    button {
        display: flex;
        align-content: center;
        align-items: center;
        justify-content: center;
        background-color: transparent;
        border: 2px solid black;
        border-radius: 10px;
        aspect-ratio: 1/1;
        cursor: pointer;
    }

    .selective {
        display: none;
    }

    @media only screen and (min-width: 500px) {
        .selective {
            display: block;
        }
    }
</style>

<style>
    #navbar.hidden {
        opacity: 0;
    }

    #buffer.hidden {
        height: 0px;
    }
</style>