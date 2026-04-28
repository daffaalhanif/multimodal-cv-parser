import base64
from pathlib import Path
from pdf2image import convert_from_path
import tempfile
import os

SUPPORTED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png"}

def load_file(file_path: str) -> list[str]:
    """
    Menerima path file (pdf atau image),
    return list of base64 encoded image string(s).
    """
    ext = Path(file_path).suffix.lower()

    if ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Format file tidak didukung: {ext}")
    
    if ext == ".pdf":
        return _pdf_to_base64(file_path)
    else:
        return [_image_to_base64(file_path)]
    
def _pdf_to_base64(pdf_path: str) -> list[str]:
    """Convert setiap halaman PDF jadi base64 image."""
    images = convert_from_path(pdf_path)
    base64_images = []

    for img in images:
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
            img.save(tmp.name, format="JPEG")
            base64_images.append(_image_to_base64(tmp.name))
            os.unlink(tmp.name)

    return base64_images

def _image_to_base64(image_path: str) -> str:
    """Convert image file jadi base64 string."""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
