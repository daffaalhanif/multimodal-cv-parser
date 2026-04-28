from typing import Annotated, Optional, List
from pydantic import BaseModel, Field, AfterValidator


def _cek_kosong(value: str) -> str:
    """Validasi nilai tidak boleh kosong atau hanya spasi."""
    if not value.strip():
        raise ValueError("Field tidak boleh kosong atau hanya spasi")
    return value


# Custom type -- str dengan validasi tidak boleh kosong
validasi = Annotated[str, AfterValidator(_cek_kosong)]


class Experience(BaseModel):
    """Schema untuk satu entri pengalaman kerja."""

    posisi: validasi
    start: validasi
    end: validasi
    description: Optional[validasi] = None


class Education(BaseModel):
    """Schema untuk satu entri pendidikan."""

    degree: validasi
    univ: validasi
    start: Optional[validasi] = None
    end: validasi
    field: validasi


class Skills(BaseModel):
    """Schema untuk kategori skills."""

    hardskills: List[validasi] = Field(default_factory=list)
    softskills: List[validasi] = Field(default_factory=list)


class CVOutput(BaseModel):
    """Schema untuk output parsing CV."""

    nama: validasi
    experience: List[Experience] = Field(default_factory=list)
    education: List[Education] = Field(default_factory=list)
    skills: Skills