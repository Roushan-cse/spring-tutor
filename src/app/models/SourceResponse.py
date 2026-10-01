from pydantic import BaseModel

class SourceResponse(BaseModel):
    lecture:int
    page : int