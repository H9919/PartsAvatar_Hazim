#Hazim's Note:   we have a list with data where we need to count the items inside and return a dictionary with the sum of appearance of each item 
# so in the function we would be creating the dictionary where if item is not in (dictionary) count_data we would append the item with count = 1
#if item is in count_data it's going to be count_data [item] += 1 at the end return the dictionary (count_data)

# Task: Dictionary Frequency Mapping
# Instructions: Return a dictionary where keys are categories 
# and values are the count of occurrences.

def count_categories(categories):
    # TODO: Write your logic here
    pass

# Test Case
data = ['Brakes', 'Engine', 'Brakes', 'Tools', 'Engine', 'Brakes']
# Expected: {'Brakes': 3, 'Engine': 2, 'Tools': 1}
print(count_categories(data))
