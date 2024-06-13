from sqlalchemy.future import select
from sqlalchemy.orm import Session
from . import models, schemas

async def create_configuration(db: Session, configuration: schemas.ConfigurationCreate):
    db_configuration = models.Configuration(country_code=configuration.country_code, requirements=configuration.requirements)
    db.add(db_configuration)
    await db.commit()
    await db.refresh(db_configuration)
    return db_configuration

async def get_configuration(db: Session, country_code: str):
    result = await db.execute(select(models.Configuration).where(models.Configuration.country_code == country_code))
    return result.scalars().first()

async def update_configuration(db: Session, country_code: str, configuration: schemas.ConfigurationUpdate):
    result = await db.execute(select(models.Configuration).where(models.Configuration.country_code == country_code))
    db_configuration = result.scalars().first()
    if db_configuration:
        db_configuration.requirements = configuration.requirements
        await db.commit()
        await db.refresh(db_configuration)
        return db_configuration
    return None

async def delete_configuration(db: Session, country_code: str):
    result = await db.execute(select(models.Configuration).where(models.Configuration.country_code == country_code))
    db_configuration = result.scalars().first()
    if db_configuration:
        await db.delete(db_configuration)
        await db.commit()
        return True
    return False
