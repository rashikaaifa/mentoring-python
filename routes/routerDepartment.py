from fastapi import APIRouter, Body, Path, Query

from controllers.controllerDepartment import DepartmentController
from models.modelDepartment import DepartmentRequestCreate, DepartmentRequestUpdate, ResponseDepartmentView
from utils.util_response import ResponseModelObjectId

ApiRouter_Department = APIRouter(
	prefix= "/department",
 	tags= ["Department"]
)

@ApiRouter_Department.get(
	"/find",
 	summary="Get All Department"
)

async def ApiRouter_Department_Find(
	name: str = Query(default=None, description="Nama Jurusan"),
	size: int = Query(default=10, ge=10, le=100, description="Jumlah Data per Halaman"),
	page: int = Query(default=1, ge=1, description="Nomor Halaman")
):
    data = DepartmentController.Find(
		name=name,
		size=size,
		page=page
	)
    return data

@ApiRouter_Department.get(
    "/get/{departmentId}",
    response_model=ResponseDepartmentView,
    summary="Get Department by Id"
)
async def ApiRouter_Department_GetById(
    departmentId: str
):
    data = DepartmentController.GetById(
        departmentId=departmentId
    )
    
    return ResponseDepartmentView(
        status_code=200,
        message="Success Get Data",
        data=data
	)

@ApiRouter_Department.post(
    "/create",
    response_model=ResponseDepartmentView,
    summary="Create Department"
)
async def ApiRouter_Department_Create(
     req: DepartmentRequestCreate = Body(
        default=...,
    )
):
    newDepartmentId = DepartmentController.Create(
        param=req
    )
    
    data = DepartmentController.GetById(
        departmentId=newDepartmentId
    )
    
    return ResponseDepartmentView(
        status_code=200,
        message="Success Get Data",
        data=data
    )
    
@ApiRouter_Department.put(
	"/update/{DepartmentId}",
 	response_model=ResponseDepartmentView,
	summary="Update Department by Id"
)
async def ApiRouter_Department_Update(
	departmentId: str,
	req: DepartmentRequestUpdate = Body(
		default=...,
 )
):
    updatedDepartmentId = DepartmentController.Update(
		departmentId=departmentId,
		param=req
	)
    
    data = DepartmentController.GetById(
		departmentId=updatedDepartmentId
	)
    
    return ResponseDepartmentView(
        status_code=200,
		message="Success Update Data",
		data=data
	)
    
@ApiRouter_Department.delete(
	"/delete/{DepartmentId}",
 	response_model=ResponseModelObjectId,
	summary="Delete Department by Id"
)
async def ApiRouter_Department_Delete(
	departmentId: str = Path(
    	default=...,
	),
):
    deletedDepartmentId = DepartmentController.Delete(
		departmentId=departmentId,
	)
    
    return ResponseModelObjectId(
		status_code=200,
		message="Success Delete Data",
		data=deletedDepartmentId
	)
    