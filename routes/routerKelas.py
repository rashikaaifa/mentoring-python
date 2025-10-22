from fastapi import APIRouter, Body, Query, Path

from controllers.controllerKelas import KelasController
from models.modelKelas import KelasRequestCreate, KelasRequestUpdate, ResponseKelasView
from utils.util_response import ResponseModelObjectId

ApiRouter_Kelas = APIRouter(
	prefix= "/kelas",
 	tags= ["Kelas"]
)

@ApiRouter_Kelas.get(
	"/find",
 	summary="Get All Kelas"
)

async def ApiRouter_Kelas_Find(
	name: str = Query(default=None, description="Tingkat"),
	size: int = Query(default=10, ge=10, le=100, description="Jumlah Data per Halaman"),
	page: int = Query(default=1, ge=1, description="Nomor Halaman")
):
    data = KelasController.Find(
		name=name,
		size=size,
		page=page
	)
    return data

@ApiRouter_Kelas.get(
    "/get/{kelasId}",
    response_model=ResponseKelasView,
    summary="Get Kelas by Id"
)
async def ApiRouter_Kelas_GetById(
    kelasId: str
):
    data = KelasController.GetById(
        kelasId=kelasId
    )
    
    return ResponseKelasView(
        status_code=200,
        message="Success Get Data",
        data=data
	)

@ApiRouter_Kelas.post(
    "/create",
    response_model=ResponseKelasView,
    summary="Create Kelas"
)
async def ApiRouter_Kelas_Create(
     req: KelasRequestCreate = Body(
        default=...,
    )
):
    newKelasId = KelasController.Create(
        param=req
    )
    
    data = KelasController.GetById(
        kelasId=newKelasId
    )
    
    return ResponseKelasView(
        status_code=200,
        message="Success Get Data",
        data=data
    )
    
@ApiRouter_Kelas.put(
	"/update/{KelasId}",
 	response_model=ResponseKelasView,
	summary="Update Kelas by Id"
)
async def ApiRouter_Kelas_Update(
	kelasId: str,
	req: KelasRequestUpdate = Body(
		default=...,
 )
):
    updatedKelasId = KelasController.Update(
		kelasId=kelasId,
		param=req
	)
    
    data = KelasController.GetById(
		kelasId=updatedKelasId
	)
    
    return ResponseKelasView(
        status_code=200,
		message="Success Update Data",
		data=data
	)
    
@ApiRouter_Kelas.delete(
	"/delete/{KelasId}",
 	response_model=ResponseModelObjectId,
	summary="Delete Kelas by Id"
)
async def ApiRouter_Kelas_Delete(
	kelasId: str = Path(
    	default=...,
	),
):
    deletedKelasId = KelasController.Delete(
		kelasId=kelasId,
	)
    
    return ResponseModelObjectId(
		status_code=200,
		message="Success Delete Data",
		data=deletedKelasId
	)
    