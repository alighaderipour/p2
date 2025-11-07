import { defineStore } from 'pinia'
import axios from 'axios'

export const useChatbotStore = defineStore('chatbot', {
  state: () => ({
    messages: []
  }),

  actions: {
    async sendMessage(prompt) {
      this.messages.push({ role: 'user', content: prompt })

      try {
        const res = await axios.post('http://127.0.0.1:8000/api/chatbot/chat/', {
          prompt
        }, {
          headers: { 'Content-Type': 'application/json' }
        })

        const botMessage = res.data.response || '⚠️ No response'
        this.messages.push({ role: 'assistant', content: botMessage })
      } catch (err) {
        console.error(err)
        this.messages.push({ role: 'assistant', content: '❌ Error connecting to server' })
      }
    }
  }
})
