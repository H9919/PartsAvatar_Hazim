#almost the same as the one before however in the code we will add a function HAVING SUM ( total_quantity) > 1
import sqlite3

def get_popular_skus():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Return SKUs where the SUM of quantity across all orders is > 1.
    query = """
    -- WRITE YOUR SQL HERE
    """
    
    cursor.execute(query)
    return cursor.fetchall()
