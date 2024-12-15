import requests
from app.config import settings
from app.manager.database import database_manager


class StabilityManager:
    def generate_image(self, outfit_description: str) -> str:
        response = requests.post(
            f"https://api.stability.ai/v2beta/stable-image/generate/core",
            headers={
                "authorization": f"Bearer {settings.STABILITY_API_KEY}",
                "accept": "image/*",
            },
            files={"none": ""},
            data={
                "prompt": outfit_description,
                "output_format": "png",
            },
        )
        if response.status_code == 200:
            session = database_manager.create_session()
            url = database_manager.storage(session, response.content, "png")
            return url
        else:
            raise Exception(str(response.json()))


stability_manager = StabilityManager()
