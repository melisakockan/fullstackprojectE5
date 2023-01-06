<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>

    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/joueur">Joueur</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/admin">Connexion</RouterLink>

      </nav>
    </div>
  </header>

  <RouterView />
</template>
