import { create } from 'zustand'

type messageStore = {
  messages: ClothingResponse[]
  updateMessages: (messages: ClothingResponse[]) => void
}

export const useMessageStore = create<messageStore>(set => ({
  messages: [],
  updateMessages: messages => set({ messages })
}))
