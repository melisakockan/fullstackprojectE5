<template>

  <div id="container">

    <div v-if="question != null" id="question_cover" :style="{ 'background-image': 'url(' + question.image + ')' }">
    </div>

    <div v-if="question != null">
      <h1>{{ pos }}/{{ tot }} : {{question.title}}</h1>

      <h2> {{question.text}}</h2>
      
      <div class="answers">
        <button v-for="(answer, index) in question.possibleAnswers" @click="selectAnswer(index)" :id="index">{{ answer.text }}</button>
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

  methods: {
    selectAnswer(index){


      for (let i = 0; i < this.question.possibleAnswers.length; i++) {
        let question_dom = document.getElementById(i);
        if (i == index  && this.question.possibleAnswers[i].isCorrect) {
          question_dom.style.backgroundColor = "#3bce87";
          question_dom.style.color = "white";
        } 
        else if (i == index && !this.question.possibleAnswers[i].isCorrect) {
          question_dom.style.backgroundColor = "#ee4266";
          question_dom.style.color = "white";
        }
        else if (this.question.possibleAnswers[i].isCorrect) {
          question_dom.style.backgroundColor = "#3bce87";
          question_dom.style.color = "white";
        }
        else {
          question_dom.style.backgroundColor = "#333333";
          question_dom.style.color = "black";
        }
      }

      // Wait 1 second before emitting the event
      setTimeout(() => {
        this.$emit('answer-selected', index+1);
        this.resetColors();
      }, 1000);

    },

    resetColors(){
      let q1 = document.getElementById(0);
      let q2 = document.getElementById(1);
      let q3 = document.getElementById(2);
      let q4 = document.getElementById(3);
      let all = [q1, q2, q3, q4];

      q1.style.backgroundColor = "#b31a85";
      q2.style.backgroundColor = "#ee4266";
      q3.style.backgroundColor = "#e8bb27";
      q4.style.backgroundColor = "#3bce87";

      let max_height = 0;
      
      for (let i = 0; i < all.length; i++) {
        all[i].style.color = "white";

        if (all[i].offsetHeight > max_height) {
          max_height = all[i].offsetHeight;
        }
      }

      for (let i = 0; i < all.length; i++) {
        all[i].style.height = max_height + "px";
      }
    }
  },

  updated(){
    this.resetColors();
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
  
  grid-gap: 6px;

  
}

.answers button{
  min-height: 60px;
  width: 100%;
  text-transform: none;
  border-radius: 0px;
  font-size: 1.2em;
  margin: 0;

  border: none;

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
