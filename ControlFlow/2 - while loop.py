# 1. Factorial ****************************************************************************************
number = 6
product = 1
current = 1
while current <= number:
    product *= current
    current += 1
print(product)


# Solution:
while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1



# 2. Factorial with for *******************************************************************************
number = 6
product = 1
for index in range(1, number+1):
    product *= index
print(product)


# Solution:
for num in range(2, number + 1):
    product *= num
print(product)



# 3. Count by Check *************************************************************************************
start_num = 90 #provide some start number
end_num = 30 #provide some end number that you stop when you hit
count_by = 1 #provide some number to count by
if start_num < end_num:
    while break_num <= end_num:
        break_num += count_by
else:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
print(result)


# Solution:
break_num = start_num
while break_num < end_num:
    break_num += count_by
print(break_num)


# Solution 2:
if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
    result = break_num
print(result)



# 4. Nearest Square *******************************************************************************
limit = 40
number = 1
while number**2 < limit:
    nearest_square = number**2
    number += 1
print(nearest_square)


# Solution:
limit = 40
num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2
print(nearest_square)



# 5. Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
num_list.sort()
index = 0
count = 0
total = 0
while count < 5 and index < len(num_list):
    # print("Test print: {} ".format(num_list[index]))
    if num_list[index] % 2 != 0:
        total += num_list[index]
        print(num_list[index])
        count += 1
        index += 1
    else:
        index += 1
print("Total: {}".format(total))
print(num_list[:10])


# Solution: it did not sort the list in order
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)
while (count_odd < 5) and (i < len_num_list):
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1
print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))
