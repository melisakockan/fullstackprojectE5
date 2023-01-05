<template>

  <div id="container">

    <div v-if="question.image" id="question_cover" :style="{ 'background-image': 'url(' + question.image + ')' }">
    </div>

    <div>
      <h1>{{ pos }}/{{ tot }} : {{question.title}}</h1>

      <h2> {{question.text}}</h2>
      
      <div class="answers">
        <button v-for="(answer, index) in question.possibleAnswers"  @click="$emit('answer-selected', index+1)">{{ answer.text }}</button>
      </div>
    </div>

    



      
  </div>

  
</template>

<script>

export default {
  props: {
    question: {
      type: Object
    },
    pos: {type: Number},
    tot: {type: Number}
  },

  emits: ['answer-selected']

}
</script>



<style>

#container{

  margin: 50px 0px;
  
  width: 100%;
  
  display: flex;

  flex-direction: column;
  
  justify-content: flex-start;
  align-items: center;


}


.answers {
  margin : auto;
  width: 60%;
  display: grid;
  grid-template-columns: 1fr 1fr;

  
}

.answers button{
  min-height: 60px;
  text-transform: none;
  border-radius: 10px;
}


#question_cover{
  width: 30%;
  min-width: 400px;
  aspect-ratio: 16/9;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;

  border-radius: 30px;
}

.answers button:nth-of-type(1){
  background-color: #b31a85;
  color: white;
}

.answers button:nth-of-type(2){
  background-color: #ee4266;
  color: white;
}

.answers button:nth-of-type(3){
  background-color: #e8bb27;
  color: white;
}

.answers button:nth-of-type(4){
  background-color: #3bce87;
  color: white;
}


@media screen and (max-width: 600px) {
  #question_cover{
    width: 80%;
    min-width: 0px;
  }


  .answers {
    width: 100%;
    grid-template-columns: 1fr;
  }

  .answers button{
    min-height: 40px;
  }
}
  



</style>
