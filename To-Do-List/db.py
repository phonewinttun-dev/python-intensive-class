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
        return {"user_id": user_data[0], "username": user_data[1]}
    else:
        return None
    
def add_tasks_db(user_id, task_name, task_status):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO tasks(user_id, task_name, task_status) VALUES (%s, %s, %s);"
    cursor.execute(query, (user_id, task_name, task_status))
    connection.commit()
    cursor.close()
    connection.close()
    return True
    

def remove_tasks_db(user_id, task_name):
    connection = get_connection()
    cursor = connection.cursor()
    query = "DELETE FROM tasks WHERE user_id = %s AND task_name = %s;"
    cursor.execute(query, (user_id, task_name))
    rows_affected = cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()
    return rows_affected > 0

def update_tasks_db(user_id, task_name):
    connection = get_connection()
    cursor = connection.cursor()
    query = "UPDATE tasks SET task_status = 'Completed' WHERE user_id = %s AND task_name = %s;"
    cursor.execute(query, (user_id, task_name))
    rows_affected = cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()
    return rows_affected > 0

def view_tasks_db(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT task_name, task_status FROM tasks WHERE user_id = %s ORDER BY created_at;"
    cursor.execute(query, (user_id))
    tasks_data = cursor.fetchall()
    connection.commit()
    cursor.close
    connection.close()
    return tasks_data
    
