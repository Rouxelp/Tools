from typing import List
from pydantic import BaseModel, Field

class Config(BaseModel):
    modules_to_export: List[str] = Field(..., description="List of modules to export from the FIT file")