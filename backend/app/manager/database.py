from typing import List
from uuid import uuid4

from app.config import settings

from supabase import Client, create_client


class DatabaseManager:
    def __init__(self):
        pass

    def create_session(self) -> Client:
        return create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

    def storage(self, client: Client, file: bytes, ext: str) -> str:
        filename = f"{uuid4()}.{ext}"
        response = client.storage.from_("clothing").upload(filename, file)
        return f"{settings.SUPABASE_URL}/storage/v1/object/public/{response.full_path}"

    def save_outfit_stlye(
        self,
        client: Client,
        url: str,
        embedding: str,
        description: str,
        description_embedding: str,
    ):
        (
            client.from_("outfit")
            .insert(
                {
                    "embedding": embedding,
                    "url": url,
                    "description": description,
                    "description_embedding": description_embedding,
                }
            )
            .execute()
        )

    def match_by_outfit(self, client: Client, embedding: List[float]):
        response = client.rpc(
            "match_outfit",
            {
                "query_embedding": embedding,
                "match_threshold": 0.5,
                "match_count": 10,
            },
        ).execute()

        return response.data

    def match_by_outfit_description(self, client: Client, embedding: List[float]):
        response = client.rpc(
            "match_outfit_description",
            {
                "query_embedding": embedding,
                "match_threshold": 0.5,
                "match_count": 10,
            },
        ).execute()

        return response.data


database_manager = DatabaseManager()
