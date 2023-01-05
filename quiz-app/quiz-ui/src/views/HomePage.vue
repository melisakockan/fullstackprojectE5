<template>
  <h1>Home page</h1>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    <p>{{ scoreEntry.date }} - {{ scoreEntry.playerName }} - {{ scoreEntry.score }}</p>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: []
    }
  },
  async created() {
    console.log("Composant Home page 'created'");
    const quizInfo = await quizApiService.getQuizInfo();
    this.registeredScores = quizInfo["data"]["scores"];
  }
};
</script>
