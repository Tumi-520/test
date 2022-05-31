from typing import Any, Dict, Generic, List, Type, TypeVar
from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.core.database import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    # Basic CRUD
    def get(self, db: Session, item_id: Any) -> ModelType | None:
        """
        Find database records by ID
        :param db: database session
        :param item_id: item id
        :return: selected data, return null if not find
        """
        return db.query(self.model).filter(self.model.id == item_id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """
        Select multiple data by limit start index and length
        :param db: database session
        :param skip: start index
        :param limit: record length
        :return: selected record list
        """
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        """
        Insert database
        :param db: database session
        :param obj_in: record which need insert
        :return: generated record
        """
        # obj_in_data = jsonable_encoder(obj_in)
        obj_dict = obj_in.dict(exclude_unset=True, exclude_none=True)
        db_obj = self.model(**obj_dict)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: ModelType, obj_in: UpdateSchemaType | Dict[str, Any]) -> ModelType:
        """
        Update database record
        :param db: database session
        :param db_obj: record which need update
        :param obj_in: the updated data
        :return: updated record
        """
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True, exclude_none=True)
        for field in update_data:
            if field in update_data and update_data[field] is not None:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, item_id: str):
        """
        Delete record by id
        :param db: database session
        :param item_id: record id
        :return: no return
        """
        if obj := db.query(self.model).filter(self.model.id == item_id).first():
            db.delete(obj)
            db.commit()

    # Group Functions
    def count_all(self, db: Session) -> int:
        """
        Get total current record count
        :param db: database session
        :return: record count
        """
        return db.query(func.count(self.model.id)).scalar()
