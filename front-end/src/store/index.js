import { createStore } from 'vuex'
import { accounts } from './modules/accounts.js'
import { notice } from './modules/notice.js'
import { survey } from './modules/survey.js'
import { quiz } from './modules/quiz.js'
import { task } from './modules/task.js'

export default createStore({
  state () {
    return {
      // 서버 기본 주소
      URL: ''
    }
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
