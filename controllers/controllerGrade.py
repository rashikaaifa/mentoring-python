import re
from typing import Any
from fastapi import HTTPException
from models.modelGrade import GradeCreate, GradeRequestCreate, GradeRequestUpdate, GradeView
from mongodb.mongoCollection import TbGrade
from repositories.repoDepartment import DepartmentRepository
from repositories.repoGrade import GradeRepository

class GradeController:
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
            
        total_items = TbGrade.count_documents(query)
        total_pages = (total_items + size - 1) // size if total_items > 0 else 0
        
        start = (page - 1) * size
        if start >= total_items and total_items > 0:
            raise HTTPException(
                  status_code=404,
                detail=f"Halaman {page} tidak ditemukan (total halaman {total_pages})"
              )
        
        grades = list(
            TbGrade.find(query)
            .skip(start)
            .limit(size)
        )
        
        for p in grades:
            p["_id"] = str(p["_id"])
        
        return {
            "data": {
                "page": page,
                "size": size,
                "total_items": total_items,
                "total_pages": total_pages,
                "items": grades
            }
        }
    
    @staticmethod
    def GetById(
        gradeId: str
    ) -> GradeView:
        data = GradeRepository.GetById(
            gradeId=gradeId
        )
        
        if not data:
            raise HTTPException(
                status_code=404,
                detail="Grade not Found"
            )
            
        return data

    @staticmethod
    def Create(
        param: GradeRequestCreate
    ):
        department = DepartmentRepository.GetById(param.departmentId)
        if not department:
            raise HTTPException(
                status_code=404,
                detail="Department not found"
            )
                        
        newDataId = GradeRepository.Create(
            param=GradeCreate(
                departmentId=param.departmentId, # relasi
                grade=param.grade,
                isDeleted=False
            )
        )

        if not newDataId:
            raise HTTPException(
                status_code=404,
                detail="Failed to Create Grade"
            )
                    
        return newDataId

    @staticmethod
    def Update(
        gradeId: str,
        param: GradeRequestUpdate
    ):
        currentData: GradeView = GradeController.GetById(
            gradeId=gradeId
        )
  
        if not GradeRepository.Update(
            gradeId=currentData.id,
            param=param.model_dump()
        ):
            raise HTTPException(
                status_code=404,
                detail="Failed to Update Grade"
            )
                    
        return currentData.id

    @staticmethod
    def Delete(
        gradeId: str,
    ):
        currentData = GradeController.GetById(
            gradeId=gradeId
        )
        
        if not GradeRepository.Update(
            gradeId=currentData.id,
            param={
                "isDeleted": True
            }
        ):
            raise HTTPException(
                status_code=500,
                detail="Failed to Delete Grade"
            )
        return currentData.id
