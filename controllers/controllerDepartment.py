import re
from typing import Any
from fastapi import HTTPException

from models.modelDepartment import DepartmentCreate, DepartmentRequestCreate, DepartmentRequestUpdate, DepartmentView
from mongodb.mongoCollection import TbDepartment
from repositories.repoDepartment import DepartmentRepository

class DepartmentController:
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
			
		total_items = TbDepartment.count_documents(query)
		total_pages = (total_items + size - 1) // size if total_items > 0 else 0
		
		start = (page - 1) * size
		if start >= total_items and total_items > 0:
			raise HTTPException(
		  		status_code=404,
				detail=f"Halaman {page} tidak ditemukan (total halaman {total_pages})"
	  		)
		
		departments = list(
			TbDepartment.find(query)
			.skip(start)
			.limit(size)
		)
		
		for p in departments:
			p["_id"] = str(p["_id"])
		
		return {
			"data": {
				"page": page,
				"size": size,
				"total_items": total_items,
				"total_pages": total_pages,
				"items": departments
			}
		}
	
	@staticmethod
	def GetById(
		departmentId: str
	) -> DepartmentView:
		data = DepartmentRepository.GetById(
			departmentId=departmentId
		)
		
		if not data:
			raise HTTPException(
				status_code=404,
				detail="Department not found"
			)
		
		return data
	
	@staticmethod
	def Create(
		param: DepartmentRequestCreate
	):
		newDataId = DepartmentRepository.Create(
			param=DepartmentCreate(
				name=param.name,
				wearpack=param.wearpack,
				desc=param.desc,
				isDeleted=False
			)
		)
		
		if not newDataId:
			raise HTTPException(
				status_code=500,
				detail="Failed to Create Department"
			)
		
		return newDataId
	
	@staticmethod
	def Update(
		departmentId: str,
		param: DepartmentRequestUpdate
	):
		currentData: DepartmentView = DepartmentController.GetById(
			departmentId=departmentId
		)
		
		if not DepartmentRepository.Update(
			departmentId=currentData.id,
			param=param.model_dump()
		):
			raise HTTPException(
				status_code=500,
				detail="Failed to Update Department"
			)
		return currentData.id
	
	@staticmethod
	def Delete(
		departmentId: str,
	):
		currentData = DepartmentController.GetById(
			departmentId=departmentId
		)
		
		if not DepartmentRepository.Update(
			departmentId=currentData.id,
			param={
				"isDeleted": True
			}
		):
			raise HTTPException(
				status_code=500,
				detail="Failed to Delete Department"
			)
		return currentData.id
