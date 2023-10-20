from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


class DrugBaseSchema(BaseModel):
    id: Optional[str]
    name: Optional[str]
    stock: Optional[int]
    created_at: Optional[int]
    updated_at: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "obat 1",
                "stock": 100,
            }
        }

class DrugResponseSchema(DrugBaseSchema):
    def dict(self, *args, **kwargs):
        kwargs["exclude_none"] = True
        return BaseModel.dict(self, *args, **kwargs)


class DrugUpdateSchema(BaseModel):
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "update obat 1",
                "stock": 200,
            }
        }


class DrugIndexResponse(BaseModel):
    status: str
    data: List[DrugResponseSchema] = []
    total: Optional[int] = Field(default=0)
    current_page: Optional[int] = Field(default=1)


class DrugCreateResponse(BaseModel):
    status: str
    data: List[DrugResponseSchema] = []


class DrugResponse(BaseModel):
    status: str
    data: DrugResponseSchema
