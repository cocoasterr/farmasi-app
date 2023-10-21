from fastapi import APIRouter, status, Depends, Request, Query
from app.schemas.drugSchemas import DrugBaseSchema, DrugUpdateSchema
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.drugs import Drugs
from app.repository.drugRepo import drugRepo
from app.serializers.drugSerializers import drugEntity, drugListEntity
from app.service.generalService import general_index, general_get_by_id, general_delete, general_update, general_create


router = APIRouter()


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_content(payloads: list[DrugBaseSchema],
                  session: Session = Depends(get_db)):
    return await general_create(Drugs, drugRepo, session, payloads)


@router.get('/')
async def index_content(request: Request,

                             page: int = Query(default=1, gt=0),
                             limit: int = Query(default=10, gt=0),
                             session: Session = Depends(get_db)) -> dict:
    return await general_index(Drugs, drugRepo, drugListEntity, page, limit)


@router.get('/{id}')
async def read_content(id: str,
                   session: Session = Depends(get_db)) -> dict:
    return await general_get_by_id(id, Drugs, drugRepo, drugEntity)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
async def delete_content(id: str,
                     session: Session = Depends(get_db)) -> dict:
    return await general_delete(id, drugRepo, drugRepo)
    
@router.put('/{id}')
async def update_content(id: str, payload: DrugUpdateSchema,
                     session: Session = Depends(get_db)):
    return await general_update(id, Drugs, session, payload)