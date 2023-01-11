<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css" integrity="sha512-MV7K8+y+gLIBoVD59lQIYicR65iaqukzvf/nwasF0nqhPay5w/9lJmVM2hMDcnK1OnMGCdVK+iQrJ7lzPJQd1w==" crossorigin="anonymous" referrerpolicy="no-referrer" />
 
  <header>

    <div class="wrapper">
      <nav>
        <RouterLink to="/">Accueil</RouterLink>
        <RouterLink to="/admin">Admin</RouterLink>
      </nav>
    </div>

    <SoundPreference/>
    <audio id="my_player" style="display: none;"></audio>
  </header>

  <RouterView />
</template>

<script>
  import SoundPreference from "@/components/SoundPreference.vue";


  export default {

    components: 
    {
        SoundPreference
    }

  }
</script>