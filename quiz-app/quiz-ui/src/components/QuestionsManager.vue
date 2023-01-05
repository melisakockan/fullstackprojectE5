<template>
  
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    
  <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" /> 
  
</template>

<script>
import QuestionDisplay from '@/components/QuestionDisplay.vue';
import quizApiService from "@/services/QuizApiService";

export default {

    data() {
        return {
            currentQuestionPosition: 1,
            totalNumberOfQuestion: 3,
            currentQuestion: null
        }
    },

    methods: {
        answerClickedHandler(answerIndex) {
            console.log('answer clicked', answerIndex);
        }
    },

    async created() {

        const question = await quizApiService.getQuestion(1);
        this.currentQuestion = question["data"];
        

    },
  

    components: 
    {
        QuestionDisplay
    }

}
</script>