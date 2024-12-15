import { useLoadingStore } from '../store/loading.store'

export function Loading() {
  const { loading } = useLoadingStore()

  return (
    <>
      {loading && (
        <div className="fixed top-0 left-0 w-full h-full bg-black/50 flex items-center justify-center z-10">
          <div className="flex flex-col items-center justify-center w-full h-full space-y-4 p-4 bg-gray-800/50">
            <div className="loader loader-dots"></div>
            <span className="text-xl font-bold">Processing...</span>
          </div>
        </div>
      )}
    </>
  )
}
