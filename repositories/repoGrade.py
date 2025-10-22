from typing import Any

from bson import ObjectId
from models.modelGrade import GradeCreate, GradeView
from mongodb.mongoCollection import TbGrade


class GradeRepository:
    @staticmethod
    def GetById(
		gradeId: str
	) -> GradeView | None:
        query: dict[str, Any] = {
			"isDeleted": False,
   			"_id": ObjectId(gradeId)
		}
        grade = TbGrade.find_one(query)
        if not grade:
            return None
        else:
            grade["_id"] = str(grade["_id"])
            return GradeView(**grade)
        
    @staticmethod
    def Create(
		param: GradeCreate
	):
        result = TbGrade.insert_one(param.model_dump())
        return str(result.inserted_id)
    
    @staticmethod
    def Update(
		gradeId: str,
		param: dict[str, Any]
	):
        result = TbGrade.update_one(
			{"_id": ObjectId(gradeId)},
			{"$set": param}
		)
        
        return(result.matched_count == 1)