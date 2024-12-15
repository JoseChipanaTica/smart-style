from typing import List

from app.core.models.embedding import embedding_model
from app.manager.database import database_manager
from app.manager.openai import openai_manager


class OutfitStylePipeline:
    def __init__(self):
        pass

    def get_image_embedding(self, img: bytes):
        embedding = embedding_model.get_embedding(img)
        return embedding

    def generate_description(self, img: bytes):
        description = openai_manager.get_outfit_descriptor(img)
        return description

    def generate_description_embedding(self, description: str) -> List[float]:
        embedding = openai_manager.description_to_embedding(description)
        return embedding

    def storage_image(self, img: bytes, ext: str):
        session = database_manager.create_session()
        url = database_manager.storage(session, img, ext)
        return url

    def save_embedding(
        self, embedding, url: str, description: str, description_embedding: str
    ):
        try:
            session = database_manager.create_session()
            database_manager.save_outfit_stlye(
                session, url, embedding, description, description_embedding
            )
            return True
        except Exception as e:
            return False

    def run(self, img: bytes, ext: str):
        embedding = self.get_image_embedding(img)
        url = self.storage_image(img, ext)
        description = self.generate_description(img)
        description_embedding = self.generate_description_embedding(description)

        self.save_embedding(embedding, url, description, description_embedding)
        return embedding
