from typing import Any, List

from app.core.models.embedding import embedding_model
from app.manager.database import database_manager
from app.manager.openai import openai_manager
from app.manager.stability import stability_manager
from app.models.response import OutfitListResponse, OutfitResponse
from app.models.strucuted_data import OutfitGenerator


class ClothingPipeline:
    def __init__(self):
        pass

    def image_to_embedding(self, img: bytes):
        embedding = embedding_model.get_embedding(img)
        return embedding

    def image_to_description(self, img: bytes):
        description = openai_manager.get_outfit_descriptor(img)
        return description

    def regenerate_description(self, description: str, user_input: str):
        if not user_input:
            return description
        new_description = openai_manager.regenerate_description(description, user_input)
        return new_description

    def description_to_embedding(self, description: str):
        embedding = openai_manager.description_to_embedding(description)
        return embedding

    def match_embedding(self, embedding) -> List[Any]:
        try:
            session = database_manager.create_session()
            outfits = database_manager.match_by_outfit(session, embedding)
            return outfits
        except Exception as e:
            return []

    def match_description_embedding(self, embedding) -> List[Any]:
        try:
            session = database_manager.create_session()
            outfits = database_manager.match_by_outfit_description(session, embedding)
            return outfits
        except Exception as e:
            return []

    def outfit_recommendation(self, clothing: str, outfits: List[Any], gender: str):
        response = openai_manager.generate_outfits(clothing, outfits, gender)
        return response

    def run(self, img: bytes, user_input: str, gender: str):
        embedding = self.image_to_embedding(img)
        image_description = self.image_to_description(img)

        description = self.regenerate_description(image_description, user_input)
        description_embedding = self.description_to_embedding(description)

        outfits_by_images = self.match_embedding(embedding)
        outfits_by_descrp = self.match_description_embedding(description_embedding)

        outfits = [i["description"] for i in outfits_by_descrp] + [
            i["description"] for i in outfits_by_images
        ]

        response: OutfitGenerator = self.outfit_recommendation(
            image_description, outfits, gender
        )

        outfit_list_response = []
        for outfit in response.outfits:
            url = stability_manager.generate_image(outfit.description)
            item = OutfitResponse(description=outfit.description, image_url=url)
            outfit_list_response.append(item)

        response = OutfitListResponse(outfits=outfit_list_response)

        return response.model_dump()
