import { createStore } from 'vuex'
import { accounts } from './modules/accounts.js'
import { notice } from './modules/notice.js'
import { task } from './modules/task.js'
import { survey } from './modules/survey.js'
import { quiz } from './modules/quiz.js'

export default createStore({
  state () {
  },
  getters() {
  },
  mutations() {
  },
  actions() {
  },
  modules: {
    accounts,
    notice,
    task,
    survey,
    quiz
  }
})
