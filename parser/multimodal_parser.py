import os
import json
import base64

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from models.schema import CVOutput

load_dotenv()


llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=1500,
    api_key=os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMPT = """You are a CV parsing assistant.
Extract structured information from the CV image.
Return ONLY valid JSON with no additional text or markdown."""

USER_PROMPT = """Extract all CV information into this exact JSON schema:

{
  "nama": "",
  "experience": [
    {
      "posisi": "",
      "start": "",
      "end": "",
      "description": null
    }
  ],
  "education": [
    {
      "degree": "",
      "univ": "",
      "start": null,
      "end": "",
      "field": ""
    }
  ],
  "skills": {
    "hardskills": [],
    "softskills": []
  }
}

Rules:
- Use null if a field is not found
- Use [] if no items found
- hardskills: technical tools, programming languages, frameworks, software
- softskills: interpersonal traits, communication, leadership
- The CV may span multiple pages -- treat all pages as one document
- Return ONLY the JSON object"""


def encode_image(image_path: str) -> str:
    """Baca file gambar dan encode ke base64 string.

    Args:
        image_path: Path ke file gambar (PNG/JPG).

    Returns:
        String base64 hasil encoding gambar.
    """
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def parse_cv(images_base64: list[str]) -> CVOutput:
    """Kirim semua halaman CV ke GPT-4o via LangChain dan ekstrak data terstruktur.

    Semua halaman dikirim dalam satu API call agar model bisa melihat
    konteks lengkap dokumen sebelum mengekstrak informasi.

    Args:
        images_base64: List of base64-encoded PNG string, satu item per halaman CV.

    Returns:
        Instance CVOutput Pydantic yang sudah tervalidasi.

    Raises:
        json.JSONDecodeError: Jika model mengembalikan JSON yang tidak valid.
        ValueError: Jika response tidak sesuai dengan schema CVOutput.
    """
    # Susun content -- semua halaman masuk dulu, prompt di akhir
    content = []
    for image_base64 in images_base64:
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{image_base64}"
            }
        })

    # Tambahkan prompt setelah semua image -- model baca semua halaman dulu
    content.append({
        "type": "text",
        "text": USER_PROMPT
    })

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=content)
    ]

    response = llm.invoke(messages)

    # LangChain mengembalikan AIMessage -- ambil string content-nya
    raw_text = response.content

    # Bersihkan markdown fence jika model tetap menyertakannya
    if "```" in raw_text:
        raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]

    raw_dict = json.loads(raw_text.strip())

    return CVOutput(**raw_dict)