from pydantic import BaseModel, Field
from typing import Optional, List


class Experience(BaseModel):
    """Schema untuk satu entri pengalaman kerja."""

    posisi: str
    start: str
    end: str
    description: Optional[str] = None


class Education(BaseModel):
    """Schema untuk satu entri pendidikan."""

    degree: str
    univ: str
    start: Optional[str] = None
    end: str
    field: str


class Skills(BaseModel):
    """Schema untuk kategori skills."""

    hardskills: List[str] = Field(default_factory=list)
    softskills: List[str] = Field(default_factory=list)


class CVOutput(BaseModel):
    """Schema untuk output parsing CV."""

    nama: str
    experience: List[Experience] = Field(default_factory=list)
    education: List[Education]   = Field(default_factory=list)
    skills: Skills