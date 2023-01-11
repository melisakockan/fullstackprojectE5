<template>

    <div id="backBtn">
        <button @click="back" class="fas fa-arrow-left"></button>
    </div>

    <h2>THEMES</h2>
    <div id="createBtn">
        <button @click="create" class="fas fa-plus"></button>
    </div>

    <div v-for="(theme, index) in themes" id="theme">
        <p>{{decodeName(theme.name)}}</p>
        <p>{{theme.volume}}</p>
        <!-- <p>{{question.text}}</p> -->
        <button @click="viewTheme(theme.id)" class="fas fa-eye"></button>
    </div>
    
  
</template>

<script>
import QuizApiService from "@/services/QuizApiService";
import soundManager from "@/services/SoundManager";


export default {
    name: 'Themes List',

    data() {
        return {
            themes: []
        }
    },

    methods: {
        back(){
            this.$emit('back', null);
        },

        decodeName(name){
            return soundManager.decodeName(name);
        },

        viewTheme(theme){
            this.$emit('theme', theme);
        },

        create(){
            this.$emit('theme', -1);
        }
    },

    emits : ['back', 'theme'],

    async created() {
        const response = await QuizApiService.getAllThemes();
        this.themes = response.data;
    },
};
</script>


<style>

#theme{
    margin: auto;
    width: 70%;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    justify-items: center;
    align-items: center;
    border-bottom: 1px solid white;
    padding: 10px 0px;
    grid-gap: 20px;
}

#theme p{
    text-align: center;
}

#theme button{
    border: none;
    color: white;
    font-size: 20px;
    cursor: pointer;
}

#theme button:hover{
    color: #0077b6;
}

#backBtn, #createBtn{
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

#backBtn button, #createBtn button{
    border: none;
    color: white;
    font-size: 20px;
    cursor: pointer;
    background-color: #0077b6;
}

#createBtn button{
    background-color: #4CAF50;
}

#createBtn button:hover{
    color: #4CAF50;
    background-color: white;
}

#backBtn button:hover{
    color: #0077b6;
    background-color: white;

}

@media screen and (max-width: 800px) {
    #theme{
        width: 100%;
        grid-template-columns: 1fr;
        grid-template-rows: 1fr 1fr 1fr;
        grid-gap: 0px;
    }


    #theme button{
        width: 30%;
    }


}


</style>