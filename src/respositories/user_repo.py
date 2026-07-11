from src.connection.database import conn


########################### FIND USER BY EMAIL ###########################
def find_user_by_email(email: str):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM Users
        WHERE email = %s
    """, (email,))

    row = cursor.fetchone()
    cursor.close()
    return row


########################### FIND USER BY ID ###########################
def find_user_by_id(user_id: int):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT *
        FROM Users
        WHERE user_id = %s
    """, (user_id,))

    row = cursor.fetchone()
    cursor.close()
    return row


########################### CREATE USER ###########################
def create_user(email: str, hashed_password: str):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Users(email, password)
        VALUES(%s, %s)
        RETURNING user_id, email
    """, (email, hashed_password))

    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    return row
