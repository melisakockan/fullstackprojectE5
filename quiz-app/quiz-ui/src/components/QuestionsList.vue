<template>

    <div v-for="(question, index) in questions" id="question">
        <p>{{question.position}}</p>
        <p>{{question.title}}</p>
        <p>{{question.text}}</p>
        <button @click="emitQuestionNumber(question.id)" class="fas fa-eye"></button>
    </div>
    
  
</template>

<script>
import QuizApiService from "@/services/QuizApiService";


export default {
    name: 'Questions List',

    data() {
        return {
            questions: []
        }
    },

    methods: {
        emitQuestionNumber(index) {
            this.$emit('question_number', index);
        }
    },

    emits : ['question_number'],

    async created() {
        const response = await QuizApiService.getAllQuestions();
        this.questions = response.data;
    },
};
</script>


<style>

#question{
    margin: auto;
    width: 70%;
    display: grid;
    grid-template-columns: 1fr 1fr 20fr 1fr;
    justify-items: center;
    align-items: center;
    border-bottom: 1px solid white;
    padding: 10px 0px;
    grid-gap: 20px;
}

#question p{
    text-align: center;
}

#question button{
    border: none;
    color: white;
    font-size: 20px;
    cursor: pointer;
}

#question button:hover{
    color: #0077b6;
}

@media screen and (max-width: 800px) {
    #question{
        width: 100%;
        grid-template-columns: 1fr;
        grid-template-rows: 1fr 1fr 1fr 1fr;
        grid-gap: 0px;
    }


    #question button{
        width: 30%;
    }


}


</style>