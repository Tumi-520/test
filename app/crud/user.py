import uuid
from typing import Union, Any, Dict
from sqlalchemy.orm import Session
from app import model
from app.core.security import get_password_hash, verify_password
from .base import CRUDBase, ModelType, CreateSchemaType, UpdateSchemaType


class CRUDUser(CRUDBase):
    def get_by_username(self, db: Session, username: str):
        return db.query(self.model).filter(self.model.username == username).first()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        while self.get(db, user_id := str(uuid.uuid4())):
            continue
        obj_in.password = get_password_hash(obj_in.password)
        obj_dict = obj_in.dict(exclude_unset=True, exclude_none=True)
        db_obj = self.model(**obj_dict, id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True, exclude_none=True)
        if update_data.get("password", None) is not None:
            update_data['password'] = get_password_hash(update_data['password'])
        for field in update_data:
            if field in update_data and update_data[field] is not None:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def auth_by_username(self, db: Session, username: str, password: str) -> ModelType:
        user_data = self.get_by_username(db, username)
        if user_data and verify_password(password, user_data.password):
            return user_data
        else:
            return None

    def auth_by_id(self, db: Session, user_id: str, password: str) -> ModelType:
        user_data = self.get(db, user_id)
        if user_data and verify_password(password, user_data.password):
            return user_data
        else:
            return None


user = CRUDUser(model.User)
