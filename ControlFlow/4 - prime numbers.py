# 1. Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]
factor = 1
is_prime = 0
not_prime = 0
for number in check_prime:
    while factor <=  number:
        if number/factor == number or number/factor == 1:
            is_prime += 1
        elif number % factor == 0:
            not_prime += 1
            divisor = factor
        factor += 1
    if is_prime == 2 and not_prime == 0:
        print("{} is a prime number".format(number))
    else:
        print("{} is not a prime number.\n  {} is one of his factors".format(number,divisor))
    factor = 1
    is_prime = 0
    not_prime = 0



# Solution: way smarter! also twoo loops, uses break.
# Logic:
# We loop through each number in the check_prime list. Create a "search-for-factors" loop beginning at 2, and continuing up to the (number-1)
# Use a conditional statement with the modulo operator to check if our number when divided by the possible factor yields any remainder besides 0.
# If we ever find one factor, we can declare that the number is not prime, and state the factor we found. Then we can break out of the loop for
# that number. If we get up to the (number - 1) and haven't broken out of the loop, then we can declare that the number is prime.
check_prime = [26, 39, 51, 53, 57, 79, 85]
for num in check_prime: # iterate through the check_prime list
    for i in range(2, num): # search for factors, iterating through numbers ranging from 2 to the number itself (actually till num - 1)
        if (num % i) == 0: # number is not prime if modulo is 0
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break
        if i == num-1: # otherwise keep checking until we've searched all possible factors, and then declare it prime
            print("{} IS a prime number".format(num))
