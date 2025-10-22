from typing import Any
from bson import ObjectId
from models.modelKelas import KelasCreate, KelasView
from mongodb.mongoCollection import TbKelas


class KelasRepository:
    @staticmethod
    def GetById(
		kelasId: str
	) -> KelasView | None:
        query: dict[str, Any] = {
			"isDeleted": False,
			"_id": ObjectId(kelasId)
		}
        kelas = TbKelas.find_one(query)
        if not kelas:
            return None
        else:
            kelas["_id"] = str(["_id"])
            return KelasView(**kelas)
        
    @staticmethod
    def Create(
		param: KelasCreate
	):
        result = TbKelas.insert_one(param.model_dump())
        return str(result.inserted_id)
    
    @staticmethod
    def Update(
		kelasId: str,
		param: dict[str, Any]
	):
        result = TbKelas.update_one(
			{"_ide": ObjectId(kelasId)},
			{"$set": param}
		)
        
        return(result.matched_count == 1)