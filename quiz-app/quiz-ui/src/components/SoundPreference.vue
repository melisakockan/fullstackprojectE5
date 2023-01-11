<template>
    <button id="audio_choose" :class="sound_class()" @click="toggleSound"></button>
</template>


<script>
    import soundManager from "@/services/SoundManager";

    export default {

        data() {
            return {
                sound_on : false
            }
        },
        async created() {
            this.sound_on = await soundManager.getSoundPreference();
        },
        methods: {
            async toggleSound(){
                soundManager.toggleSound();
                this.sound_on = await soundManager.getSoundPreference();
            },
            sound_class(){

                    if (this.sound_on == 'true'){
                        return 'fas fa-volume-up';
                    }
                    else{
                        return 'fas fa-volume-mute';
                    }
                    
                
            }
        }


   
    }
</script>

<style>
  #audio_choose{
    position: absolute;
    top: 10px;
    right: 10px;
  }

  #audio_choose:hover{
    cursor: pointer;
    color: white;
    background-color: #0077b6;
  }


</style>