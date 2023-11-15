import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => ({
    isLoggedIn: !!localStorage.getItem('token'),
    user: {
      token: localStorage.getItem('token') ?? ''
    }
  })
})
