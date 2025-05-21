def add_two(i1, i2):
	'''
    This function adds two integers.
    
    This function accepts two integers as input and returns their sum.
    '''
	return i1 + i2

def minus_two(i1, i2):
    '''
    This function subtracts one integer from the other.
    
    This function accepts two integers as input and returns their difference.
    '''
    return i1 - i2

def multiply_two(i1, i2):
    '''
    This function multiplies two integers.
    
    This function accepts two integers as input and returns their product.
    '''
    return i1 * i2

def divide_two(i1, i2):
    '''
    This function divides one integer by another.
    
    This function accepts two integers as input and returns the quotient.
    '''
    if i2 != 0:
        return i1/i2
    else:
        return 'Cannot divide by 0'