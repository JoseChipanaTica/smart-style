import { create } from 'zustand'

type loadingStore = {
  loading: boolean
  updateLoading: (loading: boolean) => void
}

export const useLoadingStore = create<loadingStore>(set => ({
  loading: false,
  updateLoading: loading => set({ loading })
}))
