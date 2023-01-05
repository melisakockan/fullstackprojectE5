<template>

    <div id="ended">
        <h1>Bravo {{ playerName }}</h1>
        <h2>Votre score est : {{score}} / {{totalNumberOfQuestion}}</h2>
        <iframe src="https://giphy.com/embed/BPJmthQ3YRwD6QqcVD" id="gif" ></iframe>
    </div>
    
</template>

  
<script>
    import participationStorageService from "@/services/ParticipationStorageService";
    import quizApiService from "@/services/QuizApiService";

    export default {

    data() {
        return {
            playerName: null,
            score: null,
            totalNumberOfQuestion: null
        }
    },
    async created() {
        this.playerName = participationStorageService.getPlayerName();
        this.score = participationStorageService.getParticipationScore();
        const quizInfo = await quizApiService.getQuizInfo();
        this.totalNumberOfQuestion = quizInfo["data"]["size"];
    }


   
  }
  </script>


<style>
    #gif{
        height: 100%;
        aspect-ratio: 16/9;
        border: none;
        overflow: hidden;
        background: transparent;
    
    }
    
    #ended{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100%;
        width: 100%;
    }
</style>