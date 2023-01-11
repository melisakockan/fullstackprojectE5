<template>
  <!-- Router button to start quiz -->
  <div id="new_quiz_container">
    <router-link to="/start-new-quiz-page" id="start_new_quiz" @click="clickNew">
      Démarrer un nouveau quiz
    </router-link>
  </div>

  <Leaderboard/>

</template>

<script>
import quizApiService from "@/services/QuizApiService";
import Leaderboard from "@/components/Leaderboard.vue";
import soundManager from "@/services/SoundManager";

export default {
  name: "HomePage",
  
  components: {
    Leaderboard
  },

  methods: {
    clickNew() {

      soundManager.playClick();
    }
  }

};
</script>



<style>


#new_quiz_container{
  margin: 50px 0px;
  text-align: center;
}


</style>