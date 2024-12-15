from typing import Any, List

from app.config import settings
from app.models.strucuted_data import OutfitGenerator
from app.utils.image import image_to_base64
from app.utils.prompt import (
    extractor_detail_system,
    generate_outfits_human,
    generate_outfits_system,
    regenerate_description_system,
)
from openai import OpenAI


class OpenAIManager:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def get_outfit_descriptor(self, img: bytes) -> str:
        base64_str = image_to_base64(img)

        messages = [
            {
                "role": "system",
                "content": extractor_detail_system,
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_str}"},
                    },
                ],
            },
        ]

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=500,
        )

        return response.choices[0].message.content

    def description_to_embedding(self, description: str) -> List[float]:
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=description,
        )

        embedding = response.data[0].embedding
        return embedding

    def regenerate_description(self, description: str, user_input: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": regenerate_description_system},
                {
                    "role": "user",
                    "content": f"This is the clothing description: {description} and user input: {user_input}",
                },
            ],
            max_tokens=500,
        )

        return response.choices[0].message.content

    def generate_outfits(self, clothing: str, similiar_outfits: List[Any], gender: str):
        response = self.client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": generate_outfits_system},
                {
                    "role": "user",
                    "content": generate_outfits_human(
                        clothing, similiar_outfits, gender
                    ),
                },
            ],
            response_format=OutfitGenerator,
        )

        return response.choices[0].message.parsed


openai_manager = OpenAIManager()
