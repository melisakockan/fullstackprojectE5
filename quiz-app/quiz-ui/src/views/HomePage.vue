<template>
  <h1>Home page</h1>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
const registeredScores = [];//!!!!!!! pas sûre de le mettre en variable globale
export default {
  name: "HomePage",
  data() {
    return registeredScores;
  },
  async created() {
    console.log("Composant Home page 'created'");
    registeredScores.push(await quizApiService.getQuizInfo()); //!!!!!!! not sure of the data obtained nous on veut le score
  }
};
</script>

