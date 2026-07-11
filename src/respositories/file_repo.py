from src.connection.database import conn


########################### GET ALL FILES IN A PROJECT ###########################
def get_files_by_project(project_id: int):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM Reviews
        WHERE project_id = %s
        ORDER BY created_at DESC
    """, (project_id,))

    rows = cursor.fetchall()
    cursor.close()
    return rows
