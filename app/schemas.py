from pydantic import BaseModel, Field
from typing import Dict, Any

class ConfigurationCreate(BaseModel):
    country_code: str = Field(..., example="IN")
    requirements: Dict[str, Any] = Field(..., example={"Business Name": "Required", "PAN": "Required", "GSTIN": "Required"})

class ConfigurationUpdate(BaseModel):
    requirements: Dict[str, Any] = Field(..., example={"Business Name": "Required", "PAN": "Required", "GSTIN": "Required"})

class Configuration(BaseModel):
    id: int
    country_code: str
    requirements: Dict[str, Any]

    class Config:
        orm_mode = True
