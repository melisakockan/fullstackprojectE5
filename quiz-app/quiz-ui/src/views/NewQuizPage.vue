<template>
  <h1>Démarrez le quiz</h1>

  <form id="start_form" @submit.prevent>
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
import soundManager from "@/services/SoundManager";

export default {
  data() {
    return {
      username: ""
    }
  },
  methods: {
    launchNewQuiz() {
      if (this.username === "") {
        alert("Veuillez entrer un nom");
        return;
      }
      soundManager.playStart();

      participationStorageService.savePlayerName(this.username);

      var Timer = setTimeout(() => {
       
        this.$router.push('/questions');
        clearTimeout(Timer);

      }, 1300);


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

#start_form input[type="text"] {
  box-sizing: border-box;
  margin: 10px;
  color: rgb(75, 75, 75);

  padding: 10px 30px;
  text-align: center;
  border-radius: 5px;

  font-size: 1.2em;

  width: 300px;

}

#start_form button {
  box-sizing: border-box;
  margin: 10px;

  padding: 10px 10px;
  text-align: center;
  border-radius: 5px;

  font-size: 1.2em;

  width: 100px;

  border: none;
}

</style>