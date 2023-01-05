<template>
  <!-- Router button to start quiz -->
  <div id="new_quiz_container">
    <router-link to="/start-new-quiz-page" id="start_new_quiz">
      Démarrer un nouveau quiz
    </router-link>
  </div>
  


  <h1>Leaderboard</h1>
  <div v-for="(scoreEntry, index) in registeredScores.slice(0, 10)" v-bind:key="scoreEntry.date" id="scores">
      <p>#{{ index+1 }}</p>
      <p>{{ scoreEntry.playerName }}</p>
      <p>{{ scoreEntry.score }}</p>
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



<style>


#scores{
  margin: 50px 0px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

#scores p{
  margin: 0;
  text-align: center;
  width: 100%;
}


#scores p:nth-child(3n){
  font-weight: bold;
  color: white;
  font-size: 1.5em;
}

#new_quiz_container{
  margin: 50px 0px;
  text-align: center;
}


</style>