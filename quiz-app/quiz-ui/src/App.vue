<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>

    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/start-new-quiz-page">Démarrer</RouterLink>
        <RouterLink to="/joueur">Joueur</RouterLink>
        <RouterLink to="/about">About</RouterLink>

      </nav>
    </div>
  </header>

  <RouterView />
</template>
