#part 1
'''
define function iterativePower with input (base and exponent variable)
    result equal to 1
    While the exponent is greater than 0
        result times base
        exponent equal to -1
    return the result from the while loop
print the iterativePower with input (base and exponent variable)
'''
def iterativePower(base, exp):
    """
    base: int or float
    exp: int >= 0
    returns: int or float, base^exp
    """
    result = 1
    while exp > 0:
        result *=base
        exp -= 1
    return result
print(iterativePower(4,8))

#part 2
'''
define function recursivePower with input (base and exponent variable)
    if exponent is less than or equal to zero
        return 1
    else:
        return the base times the recursivePower with input (base and exp-1)
print the recursivePower with input (base and exponent variable)
'''
def recursivePower(base, exp):
    """
    base: int or float
    exp: int >= 0
    returns: int or float, base^exp
    """
    if exp <= 0:
        return 1
    else: 
        return base * recursivePower(base, exp-1)
print(recursivePower(4,6))