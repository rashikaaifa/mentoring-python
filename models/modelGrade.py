from enum import Enum
from pydantic import BaseModel, Field

from utils.util_response import ResponseModel

class GradeValue(str, Enum):
    TEN = "10"
    ELEVEN = "11"
    TWELVE = "12"
    THIRTEEN = "13"

class GradeBase(BaseModel):
    grade: GradeValue = Field(
		default=...,
		title="Tingkat",
		description="Tingkatan pada struktur akademik"
	)
    
class GradeExtend(GradeBase):
    pass
    
class GradeRequestUpdate(BaseModel):
    grade: int = Field(
		default=...,
		title="Tingkat",
		description="Tingkatan pada struktur akademik"
	)
 
# relasi   
class GradeRequestCreate(GradeExtend):
    departmentId: str = Field(
		default=...,
		title="Id Department",
		description="Id dari field department"
	)

# relasi
class GradeCreate(GradeRequestCreate):
    isDeleted: bool = Field(
		default=False
	)
    
class GradeId(BaseModel):
    id: str = Field(
		default=...,
		alias="_id"
	)
    
class GradeView(GradeExtend, GradeId):
    departmentName: str = Field(
		default=""
	)

class ResponseGradeView(ResponseModel):
    data: GradeView