<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
</script>

<template>
    <Navbar></Navbar>
        <RouterView />
    <Footer></Footer>
</template>

<style>
@import '@/assets/base.css';
</style>
