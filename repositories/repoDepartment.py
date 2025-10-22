from typing import Any
from bson import ObjectId
from models.modelDepartment import DepartmentCreate, DepartmentView
from mongodb.mongoCollection import TbDepartment

class DepartmentRepository:
    @staticmethod
    def GetById(
		departmentId: str
	) -> DepartmentView | None:
        query: dict[str, Any] = {
			"isDeleted": False,
   			"_id": ObjectId(departmentId)
		}
        department = TbDepartment.find_one(query)
        if not department:
            return None
        else:
            department["_id"] = str(department["_id"])	
            return DepartmentView(**department)
        
    @staticmethod
    def Create(
		param: DepartmentCreate
	):
        result = TbDepartment.insert_one(param.model_dump())
        return str(result.inserted_id)
    
    @staticmethod
    def Update(
		departmentId: str,
  		param: dict[str, Any]
	) :
        result = TbDepartment.update_one(
			{"_id": ObjectId(departmentId)},
			{"$set": param}
		)
        
        return(result.matched_count == 1)