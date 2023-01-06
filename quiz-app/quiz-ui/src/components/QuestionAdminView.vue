<template>

    <!-- import Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css" integrity="sha512-MV7K8+y+gLIBoVD59lQIYicR65iaqukzvf/nwasF0nqhPay5w/9lJmVM2hMDcnK1OnMGCdVK+iQrJ7lzPJQd1w==" crossorigin="anonymous" referrerpolicy="no-referrer" />
 


    <div id="containerview">
           <!-- Back to Questions List -->
        <div id="actionsview">

            <button @click="$emit('question_number', null)" class="fas fa-arrow-left" style="background-color: rgb(0, 0, 201);"></button>
            <button @click="$emit('edit', true)" class="fas fa-edit" style="background-color: #02ac62;"></button>
            <button @click="deleteQuestion" class="fas fa-trash" style="background-color: #d63031;"></button>
        </div>
        <div id="questionview" v-if="question != null">
            <p>{{question.position}}</p>
            
            <h2>{{question.title}}</h2>
            <!-- Image -->
            <img v-if="question.image != null" :src="question.image" alt="" class="imageview">
            <h3>{{question.text}}</h3>

            
            
            <div class="answersview">
                <button v-for="(answer, index) in question.possibleAnswers" :class="{ correct : answer.isCorrect }">{{ answer.text }}</button>
            </div>

        </div>
    </div>
  
</template>

<script>
import QuizApiService from "@/services/QuizApiService";


export default {
    name: 'Questions Viewer',

    props: {
        question_number: {
            type: Number
        }
    },

    data() {
        return {
            question: null,
        }
    },

    methods: {
        async deleteQuestion(){
            await QuizApiService.deleteQuestion(this.question_number);
            this.$emit('question_number', null);
        },

        
     
    },

    emits: ['question_number', 'edit'],


    async created() {
        const response = await QuizApiService.getQuestion(this.question_number);
        this.question = response.data;
    }
};
</script>


<style>

#containerview{
    margin: 10px 0px;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

#actionsview{
    margin: 10px 0px;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

#actionsview button{
    margin: 10px;
    width: 150px;
    height: 50px;
    border-radius: 10px;
    border: none;
    font-size: 20px;
}

#actionsview button:hover{
    color: white;
    opacity: 0.5;

}

#questionview{
    margin: auto;
    width: 70%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

#questionview p{
    text-align: center;
}

.correct{
    background-color: green;
}

.answersview{
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    width: 50%;
}

.answersview button{
    margin: 10px;
    width: 100%;
    height: 50px;
    border-radius: 10px;
    border: none;

}

.imageview{
    height: 200px;
    aspect-ratio: 16/9;
    border-radius: 10px;
    object-fit: cover;
}

@media screen and (max-width: 800px) {
    
    .answersview{
        width: 100%;
    }

    #questionview{
        width: 100%;
    }


}
    

</style>