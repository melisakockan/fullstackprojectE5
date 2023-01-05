<template>

   
    <h1>Leaderboard</h1>
    <h2 v-if="rank != null">Votre rang est : {{rank}}</h2>
    <div v-for="(scoreEntry, index) in registeredScores.slice(0, 10)" v-bind:key="scoreEntry.date" id="scores">
        <p>#{{ index+1 }}</p>
        <p>{{ scoreEntry.playerName }}</p>
        <p>{{ scoreEntry.score }}</p>
    </div>
  </template>
  
  <script>
  import quizApiService from "@/services/QuizApiService";
  import participationStorageService from "@/services/ParticipationStorageService";
  
  export default {
    name: "HomePage",
    data() {
      return {
        registeredScores: [],
        rank: null
      }
    },
    async created() {
      const quizInfo = await quizApiService.getQuizInfo();
      this.registeredScores = quizInfo["data"]["scores"];

      let score = participationStorageService.getParticipationScore();

      if (score !== null) {
        // Compute the player's rank
        this.rank = 1;
        for (let i = 0; i < this.registeredScores.length; i++) {
          if (score < this.registeredScores[i].score) {
            this.rank++;
          }
        }
      }
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
  
  </style>