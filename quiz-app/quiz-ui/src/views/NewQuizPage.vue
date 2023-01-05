<template>
  <h1>Démarrez le quiz</h1>

  <form id="start_form">
    <div>
      <input type="text" v-model="username" id="myusername" placeholder="Entrez votre nom">
    </div>
    <button @click="launchNewQuiz">Go !</button>
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
      participationStorageService.savePlayerName(this.username);
      console.log("Launch new quiz with", this.username);
      this.$router.push('/questions');
    }

  }
}
</script>

<style>

#start_form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 80px 0px;
}

#start_form label {
  margin: 10px;
}

#start_form input {
  margin: 10px;
  color: rgb(75, 75, 75);

  padding: 10px 30px;
  text-align: center;
  border-radius: 5px;
}

</style>