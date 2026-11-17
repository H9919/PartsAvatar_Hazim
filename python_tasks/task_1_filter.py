#hAZIM'S NOTE: We have list of test_data where we need to filter and sort them in a descending order for values greater than 100. so in the function 
#we will need a for loop assuming the required time is O(n) with for loop to check the numbers one by one creating a 
#a list as a place holer named X to have the values greater than 100
#after that we woould have to sort/order them in an descending order  creating another place holder named y
# then just use .sort() function and just for edge cases also can check for 2 loops y[0] and y[1] that they are placed correctly against the rest.


# Task: List Comprehension & Filtering
# Instructions: Complete the function to return only even IDs 
# greater than 100, sorted in descending order.

def filter_orders(order_ids):
    X=[]
    for i in range order_ids:
        if order_ids[i] > 100:
            X.append(order_ids)
    y = X.sort()
    return y


# Test Case
test_data = [10, 105, 120, 44, 202, 300, 75, 110]
# Expected Output: [300, 202, 120, 110]
print(filter_orders(test_data))
