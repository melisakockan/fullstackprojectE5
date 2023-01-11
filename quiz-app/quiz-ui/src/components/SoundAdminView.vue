<template>

   

    <div id="containeredit" v-if="theme != null">
        
        <form id="my_form" @submit.prevent>
            <label for="title">Thème</label>
            <input type="text" name="name" v-model="theme_name_decoded" id="name">
            <label for="text">Volume</label>
            <input type="range" name="volume" v-model="theme.volume" min="0" max="1" step="0.01">
            <label for="image">Son</label>
            
            <SoundUpload @file-change="FileHandler"/>

            <audio v-if="theme.data" :src="sound" alt="" class="soundedit" controls :volume="theme.volume"></audio>


            <div>
                <button @click="Update" v-if="theme_id != -1" class="valider fas fa-check"></button>
                <button @click="Create" v-else class="valide fas fa-check"></button>
                <button @click="$emit('back')" style="background-color: #d66730;" class="fas fa-times"></button>
                <button @click="Delete" v-if="theme_id != -1" style="background-color: #d63031;" class="fas fa-trash"></button>
            </div>
           
           
        </form>


    </div>
  
    
  
</template>

<script>
import QuizApiService from "@/services/QuizApiService";
import soundManager from "@/services/SoundManager";
import SoundUpload from "@/components/SoundUpload.vue";


export default {
    name: 'Themes Edit',

    data() {
        return {
            theme: [],
            theme_name_decoded: null,
            originalData: null
        }
    },

    components: {
        SoundUpload
    },

    props: {
        theme_id: {
            type: Number
        }
    },

    methods: {
        back(){
            this.$emit('back', null);
        },

        decodeName(name){
            if (name == null) return null;

            return soundManager.decodeName(name);
        },

        viewTheme(theme){
            this.$emit('theme', theme);
        },

        FileHandler(file){
            
            if (file == "") {
                this.theme.data = this.originalData;
            }
            else{
                this.theme.data = file;

            }
        },

        isInputMissing(){
            if(this.theme_name_decoded == "" || this.theme.volume == "" || this.theme.data == ""){
                return true;
            }
        },

        async Update(){
            if (this.isInputMissing()) {
                alert("Veuillez remplir tous les champs");
                return;
            }

            this.theme.name = soundManager.encodeName(this.theme_name_decoded);
            const response = await QuizApiService.updateTheme(this.theme);

            if (response.status == 200){
                this.$emit('theme', null);
            }
            else{
                alert("Erreur lors de la modification du thème");
            }

        },

        async Create(){
            if (this.isInputMissing()) {
                alert("Veuillez remplir tous les champs");
                return;
            }

            this.theme.name = soundManager.encodeName(this.theme_name_decoded);
            const response = await QuizApiService.createTheme(this.theme);

            if (response.status == 200){
                this.$emit('theme', null);
            }
            else{
                alert("Erreur lors de la création du thème");
            }

        },

        async Delete(){
            const response = await QuizApiService.deleteTheme(this.theme_id);

            if (response.status == 200){
                this.$emit('theme', null);
            }
            else{
                alert("Erreur lors de la suppression du thème");
            }
        }
    },

    computed: {
        sound(){

            var data = this.theme.data;
            if (data.startsWith("data:audio")) return data;
            else{
                return "data:audio/mpeg;base64," + data;
            }
        }
    },

    emits : ['back', 'theme'],

    async created() {
        if (this.theme_id == null) return;

        if (this.theme_id == -1){
            this.theme = {
                name: "",
                volume: 0.3,
                data: ""
            }
            return;
        }

        const response = await QuizApiService.getThemeById(this.theme_id);
        this.theme = response.data;
        this.originalData = this.theme.data;
        this.theme_name_decoded = this.decodeName(this.theme.name);
    },
};
</script>


<style>

#containeredit{
    margin: 10px 0px;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

#my_form{
    margin: 10px 0px;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

#my_form input{
    margin: 10px 0px;
    width: 50%;
    border-radius: 10px;
    border: none;
    padding: 20px 10px;
    color: black;
    text-align: center;
    font-size: 17px;
}

#my_form > div{
    width: 50%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}

#my_form input[type="range"]{
    margin: 0;
    width: 50%;
    height: 20px;
    border-radius: 0px;
    border: none;
    padding: 20px 10px;

}

#my_form > div > input[type="text"]{
    width: 80%;
    border-radius: 10px;
    border: none;
    padding: 20px 10px;
    color: black;
    text-align: center;
    font-size: 17px;
}

#my_form > label{
    margin: 10px 0px;
    width: 50%;
    text-align: center;
    font-size: 20px;
}

#my_form input[type="file"]{
    margin: 10px 0px;
    width: auto;
    border-radius: 10px;
    border: none;
    padding: 20px 10px;
    color: white;
    text-align: center;
    font-size: 17px;
}


#my_form button{
    margin: 10px 10px;
    width: 30%;
    height: 50px;
    border-radius: 10px;
    border: none;
    background-color: #02ac62;
    color: white;
    font-size: 30px;
}

#my_form button:hover{
    opacity: 0.5;
}


.soundedit{
 
    border-radius: 10px;
    margin: 20px 0px;

}


@media screen and (max-width: 600px) {
    #my_form input{
        width: 80%;
    }

    #my_form > label{
        width: 80%;
    }

    #my_form > div{
        width: 80%;
    }

    #my_form button{
        width: 80%;
    }
}


</style>