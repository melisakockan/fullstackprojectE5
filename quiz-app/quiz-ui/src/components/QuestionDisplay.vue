<template>
  <h1>{{question.title}}</h1>
  <main> {{question.text}}</main>
  <img v-if="question.image" :src="question.image" />
  <div v-for="(answer, index) in question.possibleAnswers" class="answers">
    <a @click="$emit('answer-selected', index+1)">{{ answer.text }}</a>
  </div>
  
</template>

<script>

export default {
  props: {
    question: {
      type: Object
    }
  },

  emits: ['answer-selected']

}
</script>

