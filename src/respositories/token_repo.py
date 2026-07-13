from src.connection.database import conn


########################### STORE REFRESH TOKEN ###########################
def save_refresh_token(user_id: int, token: str, expires_at):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO RefreshTokens (user_id, token, expires_at)
        VALUES (%s, %s, %s)
    """, (user_id, token, expires_at))
    conn.commit()
    cursor.close()


########################### FIND REFRESH TOKEN ###########################
def find_refresh_token(token: str):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT token_id, user_id, token, expires_at, created_at
        FROM RefreshTokens
        WHERE token = %s
    """, (token,))
    row = cursor.fetchone()
    cursor.close()
    return row


########################### REVOKE SINGLE TOKEN ###########################
def revoke_refresh_token(token: str):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM RefreshTokens
        WHERE token = %s
    """, (token,))
    conn.commit()
    cursor.close()


########################### REVOKE ALL TOKENS FOR USER (full logout) ###########################
def revoke_all_user_tokens(user_id: int):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM RefreshTokens
        WHERE user_id = %s
    """, (user_id,))
    conn.commit()
    cursor.close()
