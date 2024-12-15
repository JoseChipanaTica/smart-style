from typing import List

from pydantic import BaseModel


class OutfitResponse(BaseModel):
    description: str
    image_url: str


class OutfitListResponse(BaseModel):
    outfits: List[OutfitResponse]
