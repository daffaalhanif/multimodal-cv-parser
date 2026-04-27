from typing import Annotated
from pydantic import AfterValidator, BaseModel, ValidationError

def cek_kosong(value: str) -> str:
    if not value.strip():
        raise ValueError("Tidak boleh kosong")
    return value

validasi = Annotated[str, AfterValidator(cek_kosong)]