from src.respositories import project_repo
from src.exceptions.handlers import ProjectNotFoundException, UnauthorizedProjectAccessException


########################### GET ALL PROJECTS ###########################
def get_all_projects(user_id: int):
    return project_repo.get_all_projects(user_id)


########################### CREATE PROJECT ###########################
def create_project(user_id: int, name: str, description: str):
    row = project_repo.create_project(user_id, name, description)

    return {
        "project_id": row[0],
        "user_id": row[1],
        "name": row[2],
        "description": row[3]
    }


########################### DELETE PROJECT ###########################
def delete_project(project_id: int, user_id: int):

    # Check if project exists and belongs to this user
    row = project_repo.get_project_by_id(project_id)

    if row is None:
        raise ProjectNotFoundException()

    if row[1] != user_id:
        raise UnauthorizedProjectAccessException()

    project_repo.delete_project(project_id)

    return {"message": "Project Deleted Successfully"}
