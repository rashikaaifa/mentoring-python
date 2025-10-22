from pydantic import BaseModel, Field

from utils.util_response import ResponseModel

class KelasBase(BaseModel):
    gradeId: str = Field(
		default=...,
		title="Id Grade",
		description= "Id Grade"
	)
    
class KelasExtend(KelasBase):
    pass

class KelasRequestUpdate(BaseModel):
    kelas: int = Field(
		default=...,
		title="Kelas",
		description= "Kelas"
	)
    
class KelasRequestCreate(KelasExtend):
    pass

class KelasCreate(KelasRequestCreate):
    name: str = Field(
		default=...,
		title="Kelas",
		description= "Kelas"
	)
    isDeleted: bool = Field(
		default=False
	)
    
class KelasId(BaseModel):
    id: str = Field(
        default=...,
		alias="_id"
	)
    
class KelasView(KelasExtend, KelasId):
    pass

class ResponseKelasView(ResponseModel):
    data: KelasView