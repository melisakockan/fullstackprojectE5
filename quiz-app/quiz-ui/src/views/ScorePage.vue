<template>
  
  <Score/> 

  <Leaderboard/>

  <audio id="end_player"></audio>
  
</template>

<script>
import Score from '@/components/Score.vue';
import participationStorageService from "@/services/ParticipationStorageService";
import Leaderboard from '@/components/Leaderboard.vue';

export default {

    components: 
    {
        Score,
        Leaderboard
    },

}
</script>
