#built on the previous two examples assuming the 3 tables are joined together here we can build a filter function to get customer_email and order_date 
#where ( as a case ) status ="pending" howwever case over (select customer.customer_name, sustomer.customer_email from customers where orders.statues="pending) as filter
import sqlite3

def get_pending_customers():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Select customer email and order_date where status is 'Pending'.
    query = """
    -- WRITE YOUR SQL HERE
    """
    
    cursor.execute(query)
    return cursor.fetchall()
