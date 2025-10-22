import re
from typing import Any

from fastapi import HTTPException

from models.modelKelas import KelasCreate, KelasRequestCreate, KelasRequestUpdate, KelasView
from mongodb.mongoCollection import TbKelas
from repositories.repoGrade import GradeRepository
from repositories.repoKelas import KelasRepository


class KelasController:
    @staticmethod
    def Find(
        name: str | None,
        size: int,
        page: int
    ) -> dict[str, Any]:
        query: dict[str, Any] = {
            "isDeleted": False
        }
        if name:
            query["name"] = {"$regex": re.compile(name, re.IGNORECASE)}
            
        total_items = TbKelas.count_documents(query)
        total_pages = (total_items + size - 1) // size if total_items > 0 else 0
        
        start = (page - 1) * size
        if start >= total_items and total_items > 0:
            raise HTTPException(
                  status_code=404,
                detail=f"Halaman {page} tidak ditemukan (total halaman {total_pages})"
              )
        
        kelass = list(
            TbKelas.find(query)
            .skip(start)
            .limit(size)
        )
        
        for p in kelass:
            p["_id"] = str(p["_id"])
        
        return {
            "data": {
                "page": page,
                "size": size,
                "total_items": total_items,
                "total_pages": total_pages,
                "items": kelass
            }
        }
        
    @staticmethod
    def GetById(
		kelasId: str
	) -> KelasView:
        data = KelasRepository.GetById(
			kelasId=kelasId
		)
        
        if not data:
            raise HTTPException(
				status_code=404,
				detail="Kelas not Found"
			)
            
        return data
    
    @staticmethod
    def Create(
		param: KelasRequestCreate
	):
        grade = GradeRepository.GetById(param.gradeId)
        if not grade:
            raise HTTPException(
				status_code=404,
				detail="Kelas not Found"
			)
            
        # combineName = f"{grade.grade.value} "
               
        newDataId = KelasRepository.Create(
			param=KelasCreate(
                gradeId=param.gradeId,
				# name=combineName,
				isDeleted=False
			)
		)
        
        if not newDataId:
            raise HTTPException(
				status_code=404,
				detail="Kelas not Found"
			)
            
        return newDataId
    
    @staticmethod
    def Update(
		kelasId: str,
		param: KelasRequestUpdate
	):
        currentData: KelasView = KelasController.GetById(
			kelasId=kelasId
		)
        
        if not KelasRepository.Update(
			kelasId=currentData.id,
			param=param.model_dump()
		):
            raise HTTPException(
				status_code=404,
				detail="Kelas not Found"
			)
            
        return currentData.id
    
    @staticmethod
    def Delete(
		kelasId: str
	):
        currentData = KelasController.GetById(
			kelasId=kelasId
		)
        
        if not KelasRepository.Update(
			kelasId=currentData.id,
			param={
				"isDeleted": True
			}
		):
            raise HTTPException(
				status_code=404,
				detail="Kelas not Found"
			)
            
        return currentData.id