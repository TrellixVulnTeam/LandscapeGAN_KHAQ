from PIL import Image
from io import BytesIO
import base64


def pil_to_base64(img, is_segmentation=False):
    format = "JPEG"
    if is_segmentation:
        format = "PNG"
    buffered = BytesIO()
    img.save(buffered, format=format)
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def base64_to_pil(payload):
    return Image.open(BytesIO(base64.b64decode(payload)))