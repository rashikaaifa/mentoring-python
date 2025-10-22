from fastapi import APIRouter, Body, Query, Path

from controllers.controllerGrade import GradeController
from models.modelGrade import GradeRequestCreate, GradeRequestUpdate, ResponseGradeView
from utils.util_response import ResponseModelObjectId

ApiRouter_Grade = APIRouter(
	prefix= "/grade",
 	tags= ["Grade"]
)

@ApiRouter_Grade.get(
	"/find",
 	summary="Get All Grade"
)

async def ApiRouter_Grade_Find(
	name: str = Query(default=None, description="Tingkat"),
	size: int = Query(default=10, ge=10, le=100, description="Jumlah Data per Halaman"),
	page: int = Query(default=1, ge=1, description="Nomor Halaman")
):
    data = GradeController.Find(
		name=name,
		size=size,
		page=page
	)
    return data

@ApiRouter_Grade.get(
    "/get/{gradeId}",
    response_model=ResponseGradeView,
    summary="Get Grade by Id"
)
async def ApiRouter_Grade_GetById(
    gradeId: str
):
    data = GradeController.GetById(
        gradeId=gradeId
    )
    
    return ResponseGradeView(
        status_code=200,
        message="Success Get Data",
        data=data
	)

@ApiRouter_Grade.post(
    "/create",
    response_model=ResponseGradeView,
    summary="Create Grade"
)
async def ApiRouter_Grade_Create(
     req: GradeRequestCreate = Body(
        default=...,
    )
):
    newGradeId = GradeController.Create(
        param=req
    )
    
    data = GradeController.GetById(
        gradeId=newGradeId
    )
    
    return ResponseGradeView(
        status_code=200,
        message="Success Get Data",
        data=data
    )
    
@ApiRouter_Grade.put(
	"/update/{GradeId}",
 	response_model=ResponseGradeView,
	summary="Update Grade by Id"
)
async def ApiRouter_Grade_Update(
	gradeId: str,
	req: GradeRequestUpdate = Body(
		default=...,
 )
):
    updatedGradeId = GradeController.Update(
		gradeId=gradeId,
		param=req
	)
    
    data = GradeController.GetById(
		gradeId=updatedGradeId
	)
    
    return ResponseGradeView(
        status_code=200,
		message="Success Update Data",
		data=data
	)
    
@ApiRouter_Grade.delete(
	"/delete/{GradeId}",
 	response_model=ResponseModelObjectId,
	summary="Delete Grade by Id"
)
async def ApiRouter_Grade_Delete(
	gradeId: str = Path(
    	default=...,
	),
):
    deletedGradeId = GradeController.Delete(
		gradeId=gradeId,
	)
    
    return ResponseModelObjectId(
		status_code=200,
		message="Success Delete Data",
		data=deletedGradeId
	)
    