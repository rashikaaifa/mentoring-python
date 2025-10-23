from pydantic import BaseModel, Field

from utils.util_response import ResponseModel

class KelasBase(BaseModel):
	departmentId: str = Field(
		default=...,
		title="Department Id",
		description= "Department Id"
	)
	name: str = Field(
		default=...,
		title="Kelas",
		description= "Kelas"
	)
	
class KelasExtend(KelasBase):
	pass

class KelasRequestUpdate(BaseModel):
	departmentId: str | None = Field(
		default=None,
		title="Department Id",
		description= "Department Id"
	)
	name: str | None = Field(
		default=None,
		title="Kelas",
		description= "Kelas"
	)
	
class KelasRequestCreate(KelasExtend):
	pass

class KelasCreate(KelasRequestCreate):
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