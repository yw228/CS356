<script>
export default {
    created() {
        document.getElementById('app').classList.add('loader')
        document.getElementsByTagName('html')[0].classList.add('loader')
        document.getElementsByTagName('body')[0].classList.add('loader')
    },
    unmounted() {
        document.getElementById('app').classList.remove('loader')
        document.getElementsByTagName('html')[0].classList.remove('loader')
        document.getElementsByTagName('body')[0].classList.remove('loader')
    }
}
</script>

<template>
    <video disableRemotePlayback id="loader" autoplay muted loop playsinline src="@/assets/loader.mp4"></video>
</template>

<style scoped>
    video{
        max-width: 500px;
        max-height: 500px;
        width: 30%;
        aspect-ratio: 1 / 1;
        margin: auto;
    }

    video::-internal-media-controls-overlay-cast-button {
        display: none;
    }

</style>

<style >
    #app.loader {
        display: flex;
        flex-direction: column;
        justify-content: center;
        height: 100%;
    }

    body.loader, html.loader {
        height: 100%;
        margin: 0 auto;
    }
</style>