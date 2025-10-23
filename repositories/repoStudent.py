from typing import Any
from bson import ObjectId
from models.modelStudent import StudentCreate, StudentView
from mongodb.mongoCollection import TbStudent

class StudentRepository:
    @staticmethod
    def GetById(
		studentId: str
	) -> StudentView | None:
        query: dict[str, Any] = {
			"isDeleted": False,
   			"_id": ObjectId(studentId)
		}
        department = TbStudent.find_one(query)
        if not department:
            return None
        else:
            department["_id"] = str(department["_id"])	
            return StudentView(**department)
        
    @staticmethod
    def Create(
		param: StudentCreate
	):
        result = TbStudent.insert_one(param.model_dump())
        return str(result.inserted_id)
    
    @staticmethod
    def Update(
		studentId: str,
  		param: dict[str, Any]
	) :
        result = TbStudent.update_one(
			{"_id": ObjectId(studentId)},
			{"$set": param}
		)
        
        return(result.matched_count == 1)