<template>
  <div class="chat-container">
    <h1 class="title">💬 Deepseek Chatbot</h1>

    <div class="chat-box">
      <div
        v-for="(msg, index) in messages"
        :key="index"
        :class="['message', msg.role]"
      >
        <span class="sender">{{ msg.role === 'user' ? '🧑 You' : '🤖 Deepseek' }}:</span>
        <span class="text">{{ msg.content }}</span>
      </div>
    </div>

    <form class="input-area" @submit.prevent="sendMessage">
      <input
        type="text"
        v-model="prompt"
        placeholder="Type your message..."
      />
      <button :disabled="loading">
        {{ loading ? 'Thinking...' : 'Send' }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useChatbotStore } from '../stores/chatbot'

const chatbot = useChatbotStore()
const prompt = ref('')
const loading = ref(false)

const messages = chatbot.messages

const sendMessage = async () => {
  if (!prompt.value.trim()) return
  const userMessage = prompt.value
  prompt.value = ''
  loading.value = true
  await chatbot.sendMessage(userMessage)
  loading.value = false
}
</script>

<style scoped>
.chat-container {
  max-width: 700px;
  margin: 30px auto;
  padding: 20px;
  background: #1e1e2f;
  color: #eee;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  height: 90vh;
}

.title {
  text-align: center;
  margin-bottom: 20px;
}

.chat-box {
  flex: 1;
  overflow-y: auto;
  background: #2a2a3f;
  padding: 15px;
  border-radius: 10px;
}

.message {
  margin: 8px 0;
  line-height: 1.6;
}

.message.user {
  text-align: left;
  color: #7fd1b9;
  margin-bottom: 5px;
}

.message.assistant {
  text-align: left;
  color: #f3c677;
  margin-bottom: 5px;
}

.input-area {
  display: flex;
  gap: 10px;
  margin-top: 15px;
}

input {
  flex: 1;
  padding: 10px;
  border-radius: 8px;
  border: none;
  background: #333;
  color: white;
}

button {
  padding: 10px 15px;
  background: #4a90e2;
  border: none;
  border-radius: 8px;
  color: white;
  cursor: pointer;
}

button:disabled {
  background: gray;
}
</style>
