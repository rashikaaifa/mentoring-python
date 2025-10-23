from pydantic import BaseModel, Field

from utils.util_response import ResponseModel

# field wajib
class DepartmentBase(BaseModel):
    name: str = Field(
		default=...,
  		title="Nama",
  		description="Nama jurusan di SMK RUS"
	)
    wearpackColor: str = Field(
		default=...,
  		title="Wearpack",
  		description="Warna wearpack sesuai jurusan"
	)
    
# field opsional
class DepartmentExtend(DepartmentBase):
    desc: str | None = Field(
		default=None,
  		title="Deskripsi",
  		description="Penjelasan opsional"
	)
    
# all field
class DepartmentRequestUpdate(BaseModel):
    name: str = Field(
		default=...,
  		title="Nama",
  		description="Nama jurusan di SMK RUS"
	)
    wearpackColor: str = Field(
		default=...,
  		title="Wearpack",
  		description="Warna wearpack sesuai jurusan"
	)
    desc: str | None = Field(
		default=None,
  		title="Deskripsi",
  		description="Penjelasan opsional"
	)

# pass brrti doin nothing, ini sisi fe
class DepartmentRequestCreate(DepartmentExtend):
    pass

# soft delete, sisi be
class DepartmentCreate(DepartmentExtend):
    isDeleted: bool = Field(
		default=False
	)

class DepartmentId(BaseModel):
    # bisa saja var _id dari awal, tapi best practice begini
    id: str = Field(
		default=...,
  		alias="_id"
	)
    
class DepartmentView(DepartmentExtend, DepartmentId):
    pass

class ResponseDepartmentView(ResponseModel):
    data: DepartmentView
