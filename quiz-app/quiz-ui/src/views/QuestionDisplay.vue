<template>
  <h1>question.title</h1>
  <main> question.text</main>
  <img v-if="question.image" :src="question.image" />
  <a @click="$emit('answer-selected', 2)">La réponse D</a>
</template>

<script>

export default {
  props: {
    question: {
      type: Object
    }
  }

}
</script>