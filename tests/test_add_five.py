#we have to import the function we want to test first. 
from lib.add_five import *

#Next, we create a single test example.
#THe funciton ame msut start with "test_"for python to find it.
#The rest of the function should describe what the test veriffies. 

def test_add_five_returns_eight_for_three():
# We run the function with an exampel argument 3.  
    result = add_five(3)

# And then assert that in this example it should return 8
    assert result == 8

# Pytest will run this example, and if. this example doesn't work like 
#said it would, the test will fail.

# We can put more test examples here...
def test_add_five_returns_three_for_minus_two():
    result = add_five(-2)
    assert result == 3

def test_add_five_returns_five_for_zero():
    result = add_five(0)
    assert result == 5
