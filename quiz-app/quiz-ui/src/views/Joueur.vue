<template>
  
<h1>À propos de vous</h1>

<h2>Nom du joueur : {{ playerName }}</h2>
<h2>Score : {{ score }}</h2>
  
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";

export default {

    data() {
        return {
            playerName: null,
            score: null
        }
    },
    async created() {
        this.playerName = participationStorageService.getPlayerName();
        this.score = participationStorageService.getParticipationScore();

    }


};
</script>
