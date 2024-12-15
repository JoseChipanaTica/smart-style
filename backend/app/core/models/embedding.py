from io import BytesIO

import torch
from PIL import Image
from torchvision import models, transforms


# Load a pre-trained ResNet model
class ImageEmbeddingModel:
    def __init__(self, model_name="resnet50", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = models.resnet50(pretrained=True)

        # Remove the classification layer to use the model as a feature extractor
        self.model = torch.nn.Sequential(*list(self.model.children())[:-1])
        self.model = self.model.to(self.device)
        self.model.eval()

        # Define the transformation for input images
        self.transform = transforms.Compose(
            [
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )

    def get_embedding(self, img: bytes):
        """Extract embedding from an image."""
        image = Image.open(BytesIO(img)).convert("RGB")
        input_tensor = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            embedding = self.model(input_tensor)
        return embedding.squeeze().cpu().numpy().tolist()


embedding_model = ImageEmbeddingModel()
