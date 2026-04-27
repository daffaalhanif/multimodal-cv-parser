from pydantic import BaseModel, Field
from typing import Optional, List
from parser.validator import validasi


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
    education: List[Education]   = Field(default_factory=list)
    skills: Skills