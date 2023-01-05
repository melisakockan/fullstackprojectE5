<template>
  <!-- Router button to start quiz -->
  <div id="new_quiz_container">
    <router-link to="/start-new-quiz-page" id="start_new_quiz">
      Démarrer un nouveau quiz
    </router-link>
  </div>

  <Leaderboard/>

</template>

<script>
import quizApiService from "@/services/QuizApiService";
import Leaderboard from "@/components/Leaderboard.vue";

export default {
  name: "HomePage",
  
  components: {
    Leaderboard
  },

};
</script>



<style>


#new_quiz_container{
  margin: 50px 0px;
  text-align: center;
}


</style>