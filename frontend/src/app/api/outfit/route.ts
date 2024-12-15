import { ClothingExtractorPipeline } from '@/core/pipelines/clothing-extractor.pipeline'
import { OutfitPipeline } from '@/core/pipelines/outfit.pipeline'
import { StorageDB } from '@/utils/storage'

export async function POST(request: Request) {
  try {
    const formData = await request.formData()

    const file = formData.get('file') as File
    const comment = formData.get('comment') as string

    const clothingExtractorPipeline = new ClothingExtractorPipeline()
    const outfitPipeline = new OutfitPipeline()
    const storage = new StorageDB()

    const description = await clothingExtractorPipeline.run(file)
    const outfits = await outfitPipeline.run(description)

    const urlList = []
    for (const outfit of outfits) {
      const formData = new FormData()
      formData.append('prompt', outfit)
      formData.append('output_format', 'png')

      const response = await fetch(`https://api.stability.ai/v2beta/stable-image/generate/sd3`, {
        method: 'POST',
        body: formData,
        headers: {
          Authorization: `Bearer ${process.env.STABILITY_API_KEY}`,
          Accept: 'image/*'
        }
      })

      if (response.ok) {
        const blob = await response.blob()
        const url = await storage.uploadFile(blob)

        if (url) urlList.push(url)
      }
    }

    return new Response(JSON.stringify({ urlList }), {})
  } catch (error: any) {
    console.error(error)
    return new Response(error, { status: 500 })
  }
}
