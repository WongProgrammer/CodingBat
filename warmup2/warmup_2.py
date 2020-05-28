"""
Given a string and a non-negative int n, 
return a larger string that is n copies of the original string.
"""
def string_times(str, n):
    result = ''
    for i in range(n):
        result += str
    return result

"""
Given a string an d non-negative int n, we'll say that the front of the
string is the first 3 chars, or whatever is there if the string is less than
length 3. Return n copies of the front
"""
def front_times(str, n):
    result = ''
    temp = ''
    if (len(str) < 3):
        temp += str
    else:
        temp = str[:3]

    for i in range(n):
        result += str[:3]
    return result

"""
Given a string, return a new string made of
 every other char starting with the first, so "Hello" yields "Hlo".
"""
def string_bits(str):
    result = ''
    for i in range(len(str)):
        if i % 2 == 0:
            result += str[i]
    return result

"""
Given a non-empty string like "Code" return a string like "CCcoCodCode"
"""
def string_splosion(str):
    result = ''
    for i in range(len(str)):
        result += str[:i + 1]
    return result

"""
Given a string, return the count of the number of times that a substring
length 2 appears in the string and also as the last 2 chars of the string,
so 'hixxxhi' yields 1 (we won't count the end substring).
"""
def last2(str):
    length = len(str)
    last = str[length - 2: length]
    count = 0
    end = length - 2
    for i in range(end):
        temp = str[i: i + 2]
        if temp == last:
            count = count + 1
    return count

"""
Given an array of ints, return the number of 9's in the array.
"""
def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count = count + 1
    return count

"""
Given an array of ints, return True if one of the 
    first 4 elements in the array is a 9.
The array length may be less than 4
"""
def array_front9(nums):
    length = 4
    if len(nums) < 4:
        length = len(nums)
    for i in range(length):
        if nums[i] == 9:
            return True
    return False

"""
Given an array of ints, return True if the sequence of numbers 1,2,3 
    appears in the array somewhere
"""
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False
"""

Given 2 strings, a and b, return the number of the positions
    where they contain the same length 2 substring. 
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" 
    substrings appear in the same place in both strings.
"""
def string_match(a, b):
    count = 0
    small = min(len(a), len(b))
    for i in range(small - 1):
        """
        a_sub = a[i:i+2]
        b_sub = b[i:i+2]
        if a_sub == b_sub:
        """
        if a[i] == b[i] and a[i + 1] == b[i + 1]:
            count = count + 1
    return count
print(string_match('xxcaazz', 'xxbaaz'))