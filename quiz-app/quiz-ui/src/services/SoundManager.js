import quizApiService from "@/services/QuizApiService";


export default {

    
    saveSoundPreference(soundPreference){
        localStorage.setItem('sound_on', soundPreference);
    },

    getSoundPreference(){
        if (localStorage.getItem('sound_on') === null){
            this.saveSoundPreference(false);
            return false;
        }
        return localStorage.getItem('sound_on');
    },

    toggleSound(){
        if (this.getSoundPreference() == 'false'){
            this.saveSoundPreference(true);
            var players = document.getElementsByTagName('audio');
            for (var i = 0; i < players.length; i++){
                var volume = localStorage.getItem(players[i]);
                if (volume == null || volume == 0){
                    volume = 0.3;
                }
                players[i].volume = volume;
            }

        } else {
            this.saveSoundPreference(false);
            var players = document.getElementsByTagName('audio');
            for (var i = 0; i < players.length; i++){
                localStorage.setItem(players[i], players[i].volume);
                players[i].volume = 0;
            }
        }

    },

    playSound(sound, volume = 1, player = "my_player", loop = false){


        let audio = document.getElementById(player);
        audio.pause();

        audio.src = sound;
        if (this.getSoundPreference() == 'false'){
            audio.volume = 0;
        }
        else{
            audio.volume = volume;
        }

        audio.play();

        if (loop){
            audio.addEventListener('ended', function() {
                this.currentTime = 0;
                this.play();
            }, false);
        }

        
    }, 

    async playClick(player){

        var response = await quizApiService.getSound("click");
        var new_src = this.formatB64(response.data.data);
      
        this.playSound(new_src, response.data.volume);
    },

    async playStart(){
        var response = await quizApiService.getSound("start");
        var new_src = this.formatB64(response.data.data);
      
        this.playSound(new_src, response.data.volume);
    },

    async playCorrect(){
        var response = await quizApiService.getSound("correct");
        var new_src = this.formatB64(response.data.data);
      
        this.playSound(new_src, response.data.volume);
    },

    async playWrong(){
        var response = await quizApiService.getSound("wrong");
        var new_src = this.formatB64(response.data.data);
      
        this.playSound(new_src, response.data.volume);
    },

    async playEnd(){
        var response = await quizApiService.getSound("end");
        var new_src = this.formatB64(response.data.data);
      
        this.playSound(new_src, response.data.volume);
    },

    playSoundB64(sound, volume = 1, player = "theme_player", loop = false){


        let audio = document.getElementById(player);

        var src = audio.src;

        var new_src = this.formatB64(sound);

        if (src == new_src){
            return;
        }
        
        audio.pause();
        audio.src = new_src;
        if (this.getSoundPreference() == 'false'){
            audio.volume = 0;
        }
        else{
            audio.volume = volume;
        }

        audio.play();

        if (loop){
            audio.addEventListener('ended', function() {
                this.currentTime = 0;
                this.play();
            }, false);
        }

        
    },

    encodeName(name){
        name = name.toLowerCase();

        name = name.split(' ').join('_');

        return name;
    },

    decodeName(name){
        name = name.split('_');

        for (var i = 0; i < name.length; i++){
            name[i] = name[i].charAt(0).toUpperCase() + name[i].slice(1);
        }

        name = name.join(' ');

        return name;

    },

    formatB64(b64){
        if (b64.startsWith("data:audio")) return b64;
        else{
            return "data:audio/mpeg;base64," + b64;
        }

    },

    async playTheme(theme){

        theme = this.encodeName(theme);

        var response = await quizApiService.getTheme(theme);
        this.playSoundB64(response.data.data, response.data.volume, "theme_player", true);
    }

    

}