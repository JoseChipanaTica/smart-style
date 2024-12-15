'use client'

import { Chat } from './components/chat'
import { Loading } from './components/loading'
import { Settings } from './components/settings'

export default function Home() {
  return (
    <>
      <Loading />
      <div className="h-full w-full basis-1/3 md:border-r border-gray-600/50 px-4 py-6">
        <Settings />
      </div>
      <div className="h-full w-full basis-2/3 px-4 py-2 md:py-6">
        <Chat />
      </div>
    </>
  )
}
