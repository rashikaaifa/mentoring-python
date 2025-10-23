from fastapi import APIRouter, Body, Path, Query
from controllers.controllerStudent import StudentController
from models.modelStudent import ResponseStudentView, StudentRequestCreate, StudentRequestUpdate
from utils.util_response import ResponseModelObjectId


ApiRouter_Student = APIRouter(
	prefix= "/student",
 	tags= ["Student"]
)

@ApiRouter_Student.get(
	"/find",
 	summary="Get All Student"
)

async def ApiRouter_Student_Find(
	name: str = Query(default=None, description="Nama Jurusan"),
	size: int = Query(default=10, ge=10, le=100, description="Jumlah Data per Halaman"),
	page: int = Query(default=1, ge=1, description="Nomor Halaman")
):
    data = StudentController.Find(
		name=name,
		size=size,
		page=page
	)
    return data

@ApiRouter_Student.get(
    "/get/{studentId}",
    response_model=ResponseStudentView,
    summary="Get Student by Id"
)
async def ApiRouter_Student_GetById(
    studentId: str
):
    data = StudentController.GetById(
        studentId=studentId
    )
    
    return ResponseStudentView(
        status_code=200,
        message="Success Get Data",
        data=data
	)

@ApiRouter_Student.post(
    "/create",
    response_model=ResponseStudentView,
    summary="Create Student"
)
async def ApiRouter_Student_Create(
     req: StudentRequestCreate = Body(
        default=...,
    )
):
    newstudentId = StudentController.Create(
        param=req
    )
    
    data = StudentController.GetById(
        studentId=newstudentId
    )
    
    return ResponseStudentView(
        status_code=200,
        message="Success Get Data",
        data=data
    )
    
@ApiRouter_Student.put(
	"/update/{studentId}",
 	response_model=ResponseStudentView,
	summary="Update Student by Id"
)
async def ApiRouter_Student_Update(
	studentId: str,
	req: StudentRequestUpdate = Body(
		default=...,
 )
):
    updatedstudentId = StudentController.Update(
		studentId=studentId,
		param=req
	)
    
    data = StudentController.GetById(
		studentId=updatedstudentId
	)
    
    return ResponseStudentView(
        status_code=200,
		message="Success Update Data",
		data=data
	)
    
@ApiRouter_Student.delete(
	"/delete/{studentId}",
 	response_model=ResponseModelObjectId,
	summary="Delete Student by Id"
)
async def ApiRouter_Student_Delete(
	studentId: str = Path(
    	default=...,
	),
):
    deletedstudentId = StudentController.Delete(
		studentId=studentId,
	)
    
    return ResponseModelObjectId(
		status_code=200,
		message="Success Delete Data",
		data=deletedstudentId
	)
    