import math

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        sqrt_num = int(math.sqrt(num)) + 1
        for i in range(3, sqrt_num, 2):
            if num % i == 0:
                return False
        return True
