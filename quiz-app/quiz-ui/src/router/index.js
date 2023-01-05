import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import Questions from '../views/Questions.vue'
import Score from '../views/ScorePage.vue'
import Joueur from '../views/Joueur.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/', //clair et simple car visible par le user
      name: 'home',
      component: HomePage
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
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
      path: '/joueur',
      name: 'joueur',
      component: Joueur
    }
  ]
})

export default router
