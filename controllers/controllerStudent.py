import re
from typing import Any

from fastapi import HTTPException

from models.modelStudent import StudentCreate, StudentRequestCreate, StudentRequestUpdate, StudentView
from mongodb.mongoCollection import TbStudent
from repositories.repoStudent import StudentRepository


class StudentController:
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
			
		total_items = TbStudent.count_documents(query)
		total_pages = (total_items + size - 1) // size if total_items > 0 else 0
		
		start = (page - 1) * size
		if start >= total_items and total_items > 0:
			raise HTTPException(
		  		status_code=404,
				detail=f"Halaman {page} tidak ditemukan (total halaman {total_pages})"
	  		)
		
		student = list(
			TbStudent.find(query)
			.skip(start)
			.limit(size)
		)
		
		for p in student:
			p["_id"] = str(p["_id"])
		
		return {
			"data": {
				"page": page,
				"size": size,
				"total_items": total_items,
				"total_pages": total_pages,
				"items": student
			}
		}
	
	@staticmethod
	def GetById(
		studentId: str
	) -> StudentView:
		data = StudentRepository.GetById(
			studentId=studentId
		)
		
		if not data:
			raise HTTPException(
				status_code=404,
				detail="Department not found"
			)
		
		return data
	
	@staticmethod
	def Create(
		param: StudentRequestCreate
	):
		newDataId = StudentRepository.Create(
			param=StudentCreate(
				name=param.name,
				nis=param.nis,
				kelasId=param.kelasId,
				isDeleted=False
			)
		)
		
		if not newDataId:
			raise HTTPException(
				status_code=500,
				detail="Failed to Create Student"
			)
		
		return newDataId
	
	@staticmethod
	def Update(
		studentId: str,
		param: StudentRequestUpdate
	):
		currentData: StudentView = StudentController.GetById(
			studentId=studentId
		)
		
		if not StudentRepository.Update(
			studentId=currentData.id,
			param=param.model_dump()
		):
			raise HTTPException(
				status_code=500,
				detail="Failed to Update Department"
			)
		return currentData.id
	
	@staticmethod
	def Delete(
		studentId: str,
	):
		currentData = StudentController.GetById(
			studentId=studentId
		)
		
		if not StudentRepository.Update(
			studentId=currentData.id,
			param={
				"isDeleted": True
			}
		):
			raise HTTPException(
				status_code=500,
				detail="Failed to Delete Department"
			)
		return currentData.id