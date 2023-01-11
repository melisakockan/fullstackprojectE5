<template>

 


    <div id="containeredit" v-if="question != null">
        
        <form id="my_form" @submit.prevent>
            <label for="title">Titre</label>
            <input type="text" name="title" placeholder="Titre" v-model="question.title">
            <label for="text">Texte</label>
            <input type="text" name="text" placeholder="Texte" v-model="question.text">
            <label for="image">Image</label>
            
            <ImageUpload @file-change="FileHandler"/>

            <img v-if="question.image != null" :src="question.image" alt="" class="imageedit">

            <label for="position">Position</label>
            <input type="number" name="position" placeholder="Position"  v-model="question.position">
            <label for="possibleAnswers">Réponses</label>
            <!-- Answer 1 -->
            <div v-for="(answer, index) in question.possibleAnswers" :key="index">
                <input type="checkbox" name="isCorrect" v-model="answer.isCorrect" @change="uniqueCheck(index)">
                <input type="text" placeholder="Réponse" v-model="answer.text">
            </div>
    
            <div>
                <button @click="Update" v-if="question_number > 0" class="valider fas fa-check"></button>
                <button @click="Create" v-else class="valide fas fa-check"></button>
                <button @click="$emit('edit', false)" style="background-color: #d63031;" class="fas fa-times"></button>
            </div>
           
        </form>


    </div>
  
</template>

<script>
import QuizApiService from "@/services/QuizApiService";
import ImageUpload from "@/components/ImageUpload.vue";


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
            originalImage: null
        }
    },

    components: {
        ImageUpload
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
            

        },

        FileHandler(file){
            
            if (file == "") {
                this.question.image = this.originalImage;
            }
            else{
                this.question.image = file;
            }
        },

        isInputMissing(){
            if(this.question.title == "" || this.question.text == "" || this.question.position == 0 || this.question.image == null){
                return true;
            }

            let count = 0;

            for(let i = 0; i < this.question.possibleAnswers.length; i++){
                if(this.question.possibleAnswers[i].text == ""){
                    return true;
                }
                if(this.question.possibleAnswers[i].isCorrect){
                    count++;
                }
            }

            if (count != 1) {
                return true;
            }

            return false;


        },

        async Update(){
            if (this.isInputMissing()) {
                alert("Veuillez remplir tous les champs");
                return;
            }
            const response = await QuizApiService.updateQuestion(this.question, this.question_number);
            this.$emit('edit', false);
        },

        async Create(){
            if (this.isInputMissing()) {
                alert("Veuillez remplir tous les champs");
                return;
            }
            const response = await QuizApiService.createQuestion(this.question);
            const id = response.data;
            this.$emit('question_created', id);
            this.$emit('edit', false);

        }
     
    },

    emits: ['edit', 'question_created'],


    async created() {
        if (this.question_number > 0) {
            const response = await QuizApiService.getQuestion(this.question_number);
            this.question = response.data;
            this.originalImage = this.question.image;
        }
        else{
            this.question = {
                title: "",
                text: "",
                image: null,
                position: 0,
                possibleAnswers: [
                    {
                        text: "",
                        isCorrect: false
                    },
                    {
                        text: "",
                        isCorrect: false
                    },
                    {
                        text: "",
                        isCorrect: false
                    },
                    {
                        text: "",
                        isCorrect: false
                    }
                ]
            }
        }
      
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


.imageedit{
    height: 200px;
    aspect-ratio: 16/9;
    border-radius: 10px;
    object-fit: cover;
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