<template>

        <QuestionDisplay :question="currentQuestion" :pos="currentQuestionPosition" :tot="totalNumberOfQuestion" @answer-selected="answerClickedHandler" /> 

</template>

<script>
import QuestionDisplay from '@/components/QuestionDisplay.vue';
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
import soundManager from "@/services/SoundManager";


export default {

    data() {
        return {
            currentQuestionPosition: 1,
            totalNumberOfQuestion: null,
            currentQuestion: null,
            choices: []
        }
    },

    methods: {
        async answerClickedHandler(answerIndex) {

            this.choices.push(answerIndex);
            

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
            const question = await quizApiService.getQuestionByPosition(position);
            this.currentQuestion = question["data"];
        },

        async endQuiz() {
            let playerName = participationStorageService.getPlayerName();
            let result = await quizApiService.addParticipation(playerName, this.choices);
            let score = result["data"]["score"];
            participationStorageService.saveParticipationScore(score);
            soundManager.playEnd();
            this.$router.push("/score");
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
