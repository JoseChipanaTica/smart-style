import Markdown from 'react-markdown'
import { useMessageStore } from '../store/messages.store'

export function Chat() {
  const { messages } = useMessageStore()
  return (
    <div className="w-full h-full flex flex-col space-y-4 overflow-auto">
      {messages.map((item, index) => (
        <div key={index}>
          <ChatItem
            params={{
              item
            }}
          />
          <div className="divider"></div>
        </div>
      ))}
    </div>
  )
}

function ChatItem({ params }: { params: { item: ClothingResponse } }) {
  return (
    <div className="w-full flex flex-col space-y-2">
      <Markdown>{params.item.description}</Markdown>
      <div className="carousel carousel-center rounded-box space-x-4 p-4 h-full overflow-auto">
        {params.item.outfits.map((el, index) => (
          <div
            key={index}
            className="flex flex-col space-y-4 border border-gray-600/50 p-4 rounded-lg
            overflow-auto carousel-item max-w-xs md:max-w-md items-center content-center text-justify"
          >
            <div className="basis-2/3">
              <Markdown>{el.description}</Markdown>
            </div>
            <div className="basis-1/3">
              <img src={el.image_url} height={250} width={250} alt="" className=" rounded-lg" />
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
