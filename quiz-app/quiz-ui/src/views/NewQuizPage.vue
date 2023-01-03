<template>
  <h1>Démarrez le quiz</h1>
  <div class="NewQuizPage">
  </div>

  <form>
    <div class="mb-3">
      <label for="insertusername" class="form-label">Saisissez votre nom :</label>
      <input type="text" v-model="username" class="form-control" id="myusername">
      <!--<p>{{ username }}</p>-->
    </div>
    <button class="btn btn-primary" @click="launchNewQuiz">Go !</button>
  </form>

  <!-- Le code de ce form a été inspiré de la doc bootstrap 
    https://getbootstrap.com/docs/5.0/forms/overview/-->

</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
export default {
  data() {
    return {
      username: ""
    }
  },
  methods: {
    launchNewQuiz() {
      const playerName = participationStorageService.getPlayerName();
      console.log("Launch new quiz with", this.username);
    }
  }
}
</script>

<style>
@media (min-width: 1024px) {
  .NewQuizPage {
    min-height: 50%;
    display: flex;
    align-items: center;
  }
}
</style>