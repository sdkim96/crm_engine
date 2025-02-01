from pydantic import BaseModel

class Prompt(BaseModel):
    id: str
    text: str