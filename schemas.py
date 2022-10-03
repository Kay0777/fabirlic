from pydantic import BaseModel
from pydantic import Field


class DistributionSchema(BaseModel):
    massage: str = Field(title="Distribution message", max_length=256)
    tag: str = Field(title="Distribution tag", max_length=32)


class UserSchema(BaseModel):
    phone_number: str = Field(
        title="User phone number",
        regex="^7{1}[0-9]{10}$",
        description="Fuck!!!")
    code_mobile_operator: str = Field(
        title="User Mobile Operator code", max_length=64)
    tag: str = Field(title="User tag", max_length=32)
