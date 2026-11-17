#what we have common between customers and customer orders is customer_id and between orders and order_items is order_id
# so we would be joinig orders on customers.customers_id = orders.customers_id
#and join order_items on orders.order_id = order_items.order_id
#since those are the common aspect and we can work a JOIN from there to use the 3 tables
#before that we can build a function to get the total_revenue SUM quantity as total quantity then we can create total_quantity*price as total_revenue
#order by total_revenue desc

import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = """
    -- WRITE YOUR SQL HERE
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
