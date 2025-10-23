from pydantic import BaseModel, Field

from utils.util_response import ResponseModel


class StudentBase(BaseModel):
    name: str = Field(
        default=...,
        title="Nama",
        description="Nama siswa"
    )
    nis: int = Field(
        default=...,
        title="NIS",
        description="Nomor Induk Siswa"
    )
    kelasId: str = Field(
        default=...,
        title="Kelas Id",
        description="Kelas Id"
    )
    
class StudentRequestCreate(StudentBase):
    pass
    
class StudentRequestUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        title="Nama",
        description="Nama siswa"
    )
    nis: int | None = Field(
        default=...,
        title="NIS",
        description="Nomor Induk Siswa"
    )
    kelasId: str | None = Field(
        default=...,
        title="Kelas Id",
        description="Kelas Id"
    )
    
class StudentCreate(StudentRequestCreate):
    isDeleted: bool = Field(
        default=False
    )
    
class StudentId(BaseModel):
    id: str = Field(
        default=...,
        alias="_id"
    )
    
class StudentView(StudentId, StudentRequestUpdate):
    pass

class ResponseStudentView(ResponseModel):
    data: StudentView