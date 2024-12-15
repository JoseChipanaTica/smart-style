export const clothingService = async (form: {
  files: File[]
  gender: string
  description: string
}): Promise<ClothingResponse | undefined> => {
  try {
    const formData = new FormData()
    formData.append('file', form.files[0])
    formData.append('gender', form.gender)
    formData.append('description', form.description)

    const res = await fetch('/api/clothing', {
      method: 'POST',
      body: formData
    })

    if (res.ok) {
      const response: ClothingResponse = await res.json()
      return response
    } else {
      return undefined
    }
  } catch (error) {
    console.error(error)
    return undefined
  }
}
