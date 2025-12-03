# import necessary libraries
from pydantic import BaseModel, Field, computed_field
from typing import Annotated

# define user input schema
class UserInput(BaseModel):
    age: Annotated[int,Field(
        ..., gt=0, lt=101, description="Age must be between 1 and 100"
    )]

    bmi: Annotated[int, Field(..., ge=10, lt=61, description="BMI must be between 10 and 60"
    )]

    risk_score: Annotated[float, Field(
        ..., ge=0, lt=1.1, description="Risk score must be between 0 and 100"
    )]

    chronic_count: Annotated[int, Field(
        ..., ge=0, lt=11, description="Chronic condition count must be between 0 and 10"
    )]

    provider_quality: Annotated[int, Field(
        ..., ge=0, lt=11, description="Provider quality must be between 0 and 10"
    )]

