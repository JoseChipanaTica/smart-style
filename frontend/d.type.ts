type ClothingExtraction = {
  type: string
  color: string
  features: string[]
  material?: string
  style?: string
  season?: string
  gender?: string
}

type Clothing = ClothingExtraction & {
  url: string
}

type OutiftResponse = {
  description: string
  image_url: string
}
type ClothingResponse = {
  outfits: OutiftResponse[]
  description: string
}
