# here the discount is going to be calculated in reverse making the new_discount 1-(discount/100) 
#if the discount was zero we can just multiply 1 by the price for example a price is 100 and the discount is 10 
#new_discount= 1-(10/100) = 0.9 so the price after discount 0.9*100= 90
#then to handle if discount is zero that will eb an if statemrnt if discount = 0, new discount= 1 
#so in taht case for example 100/1=100 
#ok so inside the function we would need new_price = None , new_discount= 1
#first if statement if discountpercent= 0
#new_price = price
#if discount_percentage > 0 : new discount= 1-(discount /100)
#new_price =  
# Task: Error Handling & Resilience
# Goal: Calculate a discount safely.

def calculate_discount(price, discount_percent):
    """
    Instructions: Handle cases where discount_percent is 0 
    or if inputs are strings/None. Return 0 for invalid inputs.
    """
    # TODO: Implement logic
    

# Test Case
print(calculate_discount(100, "10")) # Should return 0 or handle conversion
print(calculate_discount(100, 0))    # Should return 0
