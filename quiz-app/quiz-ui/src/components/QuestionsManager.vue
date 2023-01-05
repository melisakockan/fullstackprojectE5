<template>

    <div v-if="isOver" id="ended">
        <h1>Bravo {{ playerName }}</h1>
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
import participationStorageService from "@/services/ParticipationStorageService";


export default {

    data() {
        return {
            currentQuestionPosition: 1,
            totalNumberOfQuestion: null,
            currentQuestion: null,
            isOver: false,
            score: null,
            choices: [],
            playerName: null
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
            const question = await quizApiService.getQuestion(position);
            this.currentQuestion = question["data"];
        },

        async endQuiz() {
            this.playerName = participationStorageService.getPlayerName();
            const result = await quizApiService.addParticipation(this.playerName, this.choices);
            this.score = result["data"]["score"];
            participationStorageService.saveParticipationScore(this.score);
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
    height: 100%;
    aspect-ratio: 16/9;
    border: none;
    overflow: hidden;
    background: transparent;

}

#ended{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
}
</style>