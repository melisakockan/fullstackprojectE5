<template>

  <div id="container">

    <div v-if="question != null" id="question_cover" :style="{ 'background-image': 'url(' + question.image + ')' }">
    </div>

    <div v-if="question != null">
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

#container > div:last-of-type{
  width: 60%;
}

.answers {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;

  justify-items: center;
  align-items: center;
  

  
}

.answers button{
  min-height: 60px;
  width: 100%;
  text-transform: none;
  border-radius: 0px;
  font-size: 1.2em;
  margin: 0;
  border: 3px solid #181818;

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

  #container > div:last-of-type{
  width: 90%;
}


  .answers {
    width: 100%;
    grid-template-columns: 1fr;
    grid-gap: 0px;
  }

  .answers button{
    height: 70px;
    width: 90%;

  }
}
  



</style>
