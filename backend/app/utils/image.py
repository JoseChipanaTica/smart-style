import base64


def image_to_base64(image_bytes: bytes) -> str:
    base64_str = base64.b64encode(image_bytes).decode("utf-8")
    return base64_str
