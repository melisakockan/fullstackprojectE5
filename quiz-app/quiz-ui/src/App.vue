<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>

    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <Router-link to="/start-new-quiz-page">Démarrer</router-link>
        <RouterLink to="/joueur">Joueur</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>
