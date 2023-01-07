<script>
export default {
    methods: {
        about() {
            window.location.href = 'https://github.com/nobibiyiqi/SharkRuby'
        }
    }
}
</script>


<template>
    <footer @click="about">
        v. 1.0.0
    </footer>
</template>

<style scoped>
    footer {
        width: 100%;
        text-align: center;
        font-family: 'Inconsolata', monospace;
        font-weight: 300;
        font-size: 15px;
        color: var(--grey);
        padding: 5px;
    }
</style>