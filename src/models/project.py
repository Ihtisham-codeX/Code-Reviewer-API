from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    description: str

class ProjectResponse(BaseModel):
    project_id: int
    name: str
    description: str
    user_id: int
