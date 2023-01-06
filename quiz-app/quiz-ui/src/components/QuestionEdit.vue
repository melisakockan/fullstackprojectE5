<template>

 


    <div id="containeredit" v-if="question != null">
           <!-- Back to Questions List -->
        <div id="actionsview">
            <button @click="$emit('question_number', null)">Retour</button>
            <button @click="$emit('edit', question_number)">Éditer</button>
            <button @click="deleteQuestion">Supprimer</button>
        </div>
        
        <form id="my_form" @submit.prevent>
            <label for="title">Title</label>
            <input type="text" name="title" placeholder="Title" v-model="question.title">
            <label for="text">Text</label>
            <input type="text" name="text" placeholder="Text" v-model="question.text">
            <label for="image">Image</label>
            <input type="file" @change="encodeImageFileAsURL()">
            <label for="position">Position</label>
            <input type="number" name="position" placeholder="Position"  v-model="question.position">
            <label for="possibleAnswers">Answers</label>
            <!-- Answer 1 -->
            <div v-for="(answer, index) in question.possibleAnswers" :key="index">
                <input type="checkbox" name="isCorrect" v-model="answer.isCorrect" @change="uniqueCheck(index)">
                <input type="text" placeholder="Réponse" v-model="answer.text">
            </div>
    
    
            <button @click="">Modifier</button>
        </form>


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
        uniqueCheck(index){
            let count = 0;
            for(let i = 0; i < this.question.possibleAnswers.length; i++){
                if(this.question.possibleAnswers[i].isCorrect){
                    count++;
                }
            }
            if(count > 1){
                for(let i = 0; i < this.question.possibleAnswers.length; i++){
                    this.question.possibleAnswers[i].isCorrect = false;
                }
            }

            // Check the selected answer
            this.question.possibleAnswers[index].isCorrect = true;
            

        }
     
    },

    emits: ['question_number', 'edit'],


    async created() {
        const response = await QuizApiService.getQuestion(this.question_number);
        this.question = response.data;
    }
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

#actionsedit{
    margin: 10px 0px;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

#actionsedit button{
    margin: 10px;
    width: 150px;
    height: 50px;
    border-radius: 10px;
    border: none;
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

#my_form > div > input[type="checkbox"]{
    margin: 0;
    width: 20px;
    height: 20px;
    border-radius: 0px;
    border: none;
    padding: 20px 10px;
    color: black;
    text-align: center;
    margin-right: 10px;
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

</style>