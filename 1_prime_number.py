# Check if a number is odd or even

def prime_number(_number):
    if _number < 2:
        return "The number must be greater than 1"

    for i in range(2,_number,1):
        if _number%i==0:
            return False
    return True

print("Is prime:",prime_number(10))
