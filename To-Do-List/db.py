import psycopg2

def get_connection():
    
    connection = psycopg2.connect(
        host = "localhost",
        port = 5432,
        user = "postgres",
        password = "admin",
        dbname = "todo_db"
    )
    return connection

def add_user(username, password):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO users(username, password) VALUES (%s, %s) RETURNING user_id"
    cursor.execute(query, (username, password))
    user_id = cursor.fetchone()[0]
    cursor.close()
    connection.commit()
    connection.close()
    return user_id

def check_user_exists(username,password):
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT user_id, username FROM users WHERE username = %s AND password = %s;"
    cursor.execute(query, (username, password))
    user_data = cursor.fetchone()
    cursor.close()
    connection.close()

    if user_data:
        print(f"UserID: {user_data[0]}, Username: {user_data[1]}")
    else:
        return None