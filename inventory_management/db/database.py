import mysql.connector

def db_connection():
    """Create and return a database connection."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aditya@23",
        database="inventory_db"
    )

def execute_query(query, values=None, fetch=False):
    """Execute a query and return results if fetch is True."""
    conn = db_connection()
    cursor = conn.cursor()
    
    if values:
        cursor.execute(query, values)
    else:
        cursor.execute(query)

    if fetch:
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    
    conn.commit()
    cursor.close()
    conn.close()