import { useState } from 'react'
import { toast } from 'react-toastify'
import { clothingService } from '../services/clothing.service'
import { useLoadingStore } from '../store/loading.store'
import { useMessageStore } from '../store/messages.store'

export function Settings() {
  const [clothingForm, setClothingForm] = useState<{ files: File[]; gender: string; description: string }>({
    files: [],
    gender: '',
    description: ''
  })

  const { messages, updateMessages } = useMessageStore()
  const { updateLoading } = useLoadingStore()

  const askStyle = async () => {
    if (clothingForm.files.length === 0) {
      return
    }

    updateLoading(true)
    const response = await clothingService(clothingForm)

    if (!response) {
      toast.error('Failed to get style')
      updateLoading(false)
      return
    }

    messages.push(response)
    updateMessages(messages)
    toast.success('Style generated')
    updateLoading(false)
  }
  return (
    <div className="w-full h-full flex flex-col space-y-4">
      <div>
        <label className="form-control w-full">
          <div className="label">
            <span className="label-text">File</span>
          </div>
          <input
            type="file"
            className="file-input input-bordered w-full"
            onChange={e => {
              if (e.target.files) {
                setClothingForm({ ...clothingForm, files: Array.from(e.target.files) })
              }
            }}
          />
        </label>
      </div>

      <div>
        <label className="form-control w-full">
          <div className="label">
            <span className="label-text">Gender</span>
          </div>
          <select
            className="select select-bordered"
            value={clothingForm.gender}
            onChange={e => {
              setClothingForm({ ...clothingForm, gender: e.target.value })
            }}
          >
            <option value={'woman'}>Woman</option>
            <option value={'man'}>Man</option>
            <option value={'non-binanry'}>Non-binary</option>
          </select>
        </label>
      </div>

      <div>
        <label className="form-control w-full">
          <div className="label">
            <span className="label-text">Description</span>
          </div>
          <input
            className="input input-bordered w-full"
            value={clothingForm.description}
            placeholder="I'm going to a party, what should I wear?"
            onChange={e => {
              setClothingForm({ ...clothingForm, description: e.target.value })
            }}
          />
        </label>
      </div>

      <div className="divider"></div>

      <button
        className="btn btn-primary"
        onClick={() => {
          askStyle()
        }}
      >
        Imagine
      </button>
    </div>
  )
}
