from typing import List

from pydantic import BaseModel, Field


class OutfitDescriptor(BaseModel):
    description: str = Field(
        ..., description="Outfit's description. Very detailed and specific."
    )


class OutfitGenerator(BaseModel):
    outfits: List[OutfitDescriptor]
