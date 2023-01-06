import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import Questions from '../views/Questions.vue'
import Score from '../views/ScorePage.vue'
import Joueur from '../views/Joueur.vue'
import Admin from '../views/Admin.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/', //clair et simple car visible par le user
      name: 'home',
      component: HomePage
    },
    {
      path: '/start-new-quiz-page', //clair et simple car visible par le user
      name: 'quiz',
      component: NewQuizPage
    },
    {
      path: '/questions',
      name: 'questions',
      component: Questions
    },
    {
      path: '/score',
      name: 'score',
      component: Score
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin
    }
  ]
})

export default router
