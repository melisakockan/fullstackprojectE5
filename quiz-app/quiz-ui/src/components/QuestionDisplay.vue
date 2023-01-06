<template>

  <div id="container">

    <div v-if="question != null" id="question_cover" :style="{ 'background-image': 'url(' + question.image + ')' }">
    </div>

    <div v-if="question != null">
      <h1>{{ pos }}/{{ tot }} : {{question.title}}</h1>

      <h2> {{question.text}}</h2>

      <!-- Time bar -->
      <div id="timebar">
        <div></div>
        <div></div>
      </div>
      
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

  data(){
    return {
      time: null,
      myTimer: null,
      maxtime: 200    }
  },

  methods: {
    selectAnswer(index){
      // Disable click on all buttons
      let all = document.getElementsByClassName("answers")[0].children;
      for (let i = 0; i < all.length; i++) {
        all[i].style.cursor = "default";
        all[i].style.pointerEvents = "none";
      }

      // Stop the timer
      clearTimeout(this.myTimer);

      

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
        this.time = this.maxtime;
        let timebar = document.getElementById("timebar");
        timebar.children[1].style.width = 100 + "%";
        this.setColor(100);
        this.$emit('answer-selected', index+1);
        this.resetColors();
        // Enable click on all buttons
        let all = document.getElementsByClassName("answers")[0].children;
        for (let i = 0; i < all.length; i++) {
          all[i].style.cursor = "pointer";
          all[i].style.pointerEvents = "auto";
        }

      }, 1000);

    },

    resetColors(){
      let q1 = document.getElementById(0);
      let q2 = document.getElementById(1);
      let q3 = document.getElementById(2);
      let q4 = document.getElementById(3);
      let all = [q1, q2, q3, q4];

      let max_height = 0;
      
      for (let i = 0; i < all.length; i++) {
        all[i].style.backgroundColor = "#0077b6";
        all[i].style.color = "white";

        if (all[i].offsetHeight > max_height) {
          max_height = all[i].offsetHeight;
        }
      }

      for (let i = 0; i < all.length; i++) {
        all[i].style.height = max_height + "px";
      }
    },

 
    Timer() {
      let timebar = document.getElementById("timebar");
      if (this.time > 0) {
        clearTimeout(this.myTimer);
        this.myTimer = setTimeout(() => {
          this.time -= 1;
          let percentage = (this.time/this.maxtime) * 100;
          timebar.children[1].style.width = percentage + "%";
          this.setColor(percentage);
          this.Timer();
        }, 100);
      }
      else{
        
        this.selectAnswer(-1);
      }
    },


    setColor(percentage){
      let timebar = document.getElementById("timebar");
      if (percentage > 50) {
        timebar.children[1].style.backgroundColor = "#3bce87";
      }
      else if (percentage > 25) {
        timebar.children[1].style.backgroundColor = "#e8bb27";
      }
      else {
        timebar.children[1].style.backgroundColor = "#ee4266";
      }
    }
  },

  updated(){
    this.resetColors();
    this.Timer();
  },

  created(){
    this.time = this.maxtime;
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

#timebar > div:first-of-type{
  width: 100%;
  height: 10px;
  background-color: #333333;
  border-radius: 10px;
  margin: 20px 0px;
}

#timebar > div:last-of-type{
  width: 100%;
  height: 10px;
  background-color: #b31a85;
  border-radius: 10px;
  position: relative;
  
  top : -30px;

  transition: 0.3s ease-out;

}



</style>
