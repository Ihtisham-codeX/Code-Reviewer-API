from src.connection.database import conn


########################### GET ALL PROJECTS ###########################
def get_all_projects(user_id: int):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM Projects
        WHERE user_id = %s
    """, (user_id,))

    rows = cursor.fetchall()
    cursor.close()

    projects = []
    for row in rows:
        projects.append({
            "project_id": row[0],
            "user_id": row[1],
            "name": row[2],
            "description": row[3]
        })

    return projects


########################### GET PROJECT BY ID ###########################
def get_project_by_id(project_id: int):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM Projects
        WHERE project_id = %s
    """, (project_id,))

    row = cursor.fetchone()
    cursor.close()
    return row


########################### CREATE PROJECT ###########################
def create_project(user_id: int, name: str, description: str):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Projects(user_id, name, description)
        VALUES(%s, %s, %s)
        RETURNING project_id, user_id, name, description
    """, (user_id, name, description))

    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    return row


########################### DELETE PROJECT ###########################
def delete_project(project_id: int):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Projects
        WHERE project_id = %s
    """, (project_id,))

    conn.commit()
    cursor.close()
