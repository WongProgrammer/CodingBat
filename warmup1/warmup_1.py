# sleep_in
def sleep_in(weekday, vacation):
  result = False
  if weekday == False or vacation == True:
    result = True
  return result
"""
print(sleep_in(False, True))
print(sleep_in(True, False))
print(sleep_in(False, True))
print(sleep_in(True, True))
"""

# monkey_trouble
# is to check if it refers to the same obj
# == value equality
def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True 
    return False
"""
print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))
print(monkey_trouble(False, True))
"""

# Given two int values, return their sum.
# Unless the two values are the same, then return double their sum.
def sum_double(a, b):
    result = a + b
    if a == b:
        result = result * 2
    return result
"""
print(sum_double(2,2))
print(sum_double(3,2))
"""

# Given an int n, return the absolute difference between n and 21, 
# except return double the absolute difference if n is over 21.
def diff21(n):
    result = abs(n - 21)
    if n > 21:
        result = 2 * result
    return result
"""
print(diff21(19))
print(diff21(30))
"""

# We have a loud talking parrot.
# The "hour" parameter is the current hour time in the range 0..23. 
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
# Return True if we are in trouble.
def parrot_trouble(talking, hour):
    if talking == True and hour in range(7, 20):
        return True
    return False

"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
"""
def makes10(a,b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    return False

"""
Given an int n, return True if it is within 10 of 100 or 200.
Note: abs(num) computes the absolute value of a number.
"""
def near_hundred(n):
    near_one = abs(n - 100)
    near_two = abs(n - 200)
    if near_one <= 10 or near_two <= 10:
        return True
    return False

"""
Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, then return True only if both are negative.
"""
def pos_neg(a,b,negative):
    if negative == True and a < 0 and b < 0:
        return True
    elif (negative == False and a < 0 and b > 0) or (negative == False and a > 0 and b < 0):
        return True 
    return False

"""
Given a string, return a new string where "not" has been added to the front.
However, if the string already begins with "not", return the string unchanged.

if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3
"""
def not_string(str):
    if str == 'not':
        return str
    elif str.find('not ') == -1:
        return 'not ' + str
    return str

"""
Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string 
(i.e. n will be in the range 0..len(str)-1 inclusive).
"""
def missing_char(str, n):
    return str[:n] + str[n+1:len(str)]

"""
Given a string, return a new string where the first and last chars have
been exchanged.
"""
def front_back(str):
    if len(str) > 1:
        return str[len(str) - 1:len(str)] + str[1:len(str) - 1] + str[:1]
    return str

"""
Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.
"""
def front3(str):
    if(len(str) < 3):
        return str + str + str
    three = str[:3]
    return three + three + three
