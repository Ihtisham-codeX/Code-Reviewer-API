from fastapi import APIRouter, Depends
from src.models.project import ProjectCreate
from src.services import project_service
from src.security.dependencies import get_current_user

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


# Get all my projects
@router.get("/")
def get_projects(current_user = Depends(get_current_user)):
    return project_service.get_all_projects(current_user["user_id"])


# Create a new project
@router.post("/")
def create_project(project: ProjectCreate, current_user = Depends(get_current_user)):
    return project_service.create_project(
        current_user["user_id"],
        project.name,
        project.description
    )


# Delete a project
@router.delete("/{project_id}")
def delete_project(project_id: int, current_user = Depends(get_current_user)):
    return project_service.delete_project(project_id, current_user["user_id"])
