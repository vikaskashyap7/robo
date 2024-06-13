from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from . import schemas, crud
from ..database import get_db

router = APIRouter(prefix="/configurations", tags=["configurations"])

@router.post("/", response_model=schemas.Configuration)
async def create_configuration(configuration: schemas.ConfigurationCreate, db: AsyncSession = Depends(get_db)):
    db_configuration = await crud.get_configuration(db, country_code=configuration.country_code)
    if db_configuration:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Configuration already exists")
    return await crud.create_configuration(db=db, configuration=configuration)

@router.get("/{country_code}", response_model=schemas.Configuration)
async def get_configuration(country_code: str, db: AsyncSession = Depends(get_db)):
    db_configuration = await crud.get_configuration(db, country_code=country_code)
    if not db_configuration:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Configuration not found")
    return db_configuration

@router.post("/{country_code}", response_model=schemas.Configuration)
async def update_configuration(country_code: str, configuration: schemas.ConfigurationUpdate, db: AsyncSession = Depends(get_db)):
    db_configuration = await crud.update_configuration(db=db, country_code=country_code, configuration=configuration)
    if not db_configuration:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Configuration not found")
    return db_configuration

@router.delete("/{country_code}", response_model=bool)
async def delete_configuration(country_code: str, db: AsyncSession = Depends(get_db)):
    success = await crud.delete_configuration(db=db, country_code=country_code)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Configuration not found")
    return success
