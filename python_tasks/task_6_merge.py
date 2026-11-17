#so we would be creating a forl loop to get the data from the first dictionary insering them in a newly built dictionary after getting all the data from the dictionary 
# in another for loop we can check if item is in the newly built dictionary we can aggregate the quantity if not create a new key with the name
#and add that quantity



# Task: Merging and Updating Data
# Instructions: Merge two dictionaries representing inventory updates. 
# If a key exists in both, the value from 'updates' should overwrite 'current'.

def update_inventory(current, updates):
    # TODO: Implement merge logic
    pass

# Test Case
current_inv = {'Brakes': 10, 'Oil': 5}
new_stock = {'Oil': 20, 'Filters': 15}
# Expected: {'Brakes': 10, 'Oil': 20, 'Filters': 15}
print(update_inventory(current_inv, new_stock))
