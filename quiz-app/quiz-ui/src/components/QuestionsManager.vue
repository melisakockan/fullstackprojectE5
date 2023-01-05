<template>

    <div v-if="isOver">
        <h1>Quiz Ended</h1>
        <h2>Your Score is : {{score}} / {{totalNumberOfQuestion}}</h2>
        <iframe src="https://giphy.com/embed/BPJmthQ3YRwD6QqcVD" id="gif" ></iframe>
    </div>

    <div v-else>
        <QuestionDisplay :question="currentQuestion" :pos="currentQuestionPosition" :tot="totalNumberOfQuestion" @answer-selected="answerClickedHandler" /> 
    </div>
        
    

</template>

<script>
import QuestionDisplay from '@/components/QuestionDisplay.vue';
import quizApiService from "@/services/QuizApiService";

export default {

    data() {
        return {
            currentQuestionPosition: 1,
            totalNumberOfQuestion: null,
            currentQuestion: null,
            isOver: false,
            score: null
        }
    },

    methods: {
        async answerClickedHandler(answerIndex) {
            

            if (this.currentQuestionPosition >= this.totalNumberOfQuestion) {
                this.endQuiz();
                return;
            }
            else{
                this.currentQuestionPosition++;
                await this.loadQuestionByPosition(this.currentQuestionPosition);
            }
            

        },

        async loadQuestionByPosition(position) {
            const question = await quizApiService.getQuestion(position);
            this.currentQuestion = question["data"];
        },

        async endQuiz() {
            alert("Quiz Ended");
            this.isOver = true;
        }
    },

    async created() {

        await this.loadQuestionByPosition(1);
        const quizInfo = await quizApiService.getQuizInfo();

        this.totalNumberOfQuestion = (quizInfo["data"]["size"]);
        

    },
  

    components: 
    {
        QuestionDisplay
    }

}
</script>


<style>
#gif{
    width: 100%;
    height: 100%;
    border: none;
    overflow: hidden;
    background: transparent;
}
</style>