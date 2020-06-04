"""
Given a string, return a string where for every char in the original, there are two chars.
"""
def double_char(str):
    result = ""
    for i in str:
        result += i + i
    return result

"""
Return the number of times that the string "hi" appears anywhere in the given string.
"""
def count_hi(str):
    count = 0
    for i in range(len(str) - 1):
        if(str[i: i+2]) == 'hi':
            count = count + 1
    return count

"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.
"""
def cat_dog(str):
    cat = 0
    dog = 0
    for i in range(len(str) - 2):
        if (str[i: i+3]) == 'cat':
            cat = cat + 1
        if (str[i: i+3]) == 'dog':
            dog = dog + 1

    if cat == dog:
        return True
    else: 
        return False

"""
Return the number of times that the string "code" appears anywhere in the given string, 
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.
"""
def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        temp = str[i:i+4]
        if temp[0] == 'c' and temp[1] == 'o' and temp[3] == 'e':
            count = count + 1
    return count

"""
Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string.

a = a.lower()
b = b.lower()
return (b.endswith(a) or a.endswith(b))

"""
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if len(a) >= len(b):
        return a[len(a) - len(b):len(a)] == b
    else:
        return b[len(b) - len(a):len(b)] == a

"""
Return True if the given string contains an appearance of 
    "xyz" where the xyz is not directly preceeded by a period (.). 
So "xxyz" counts but "x.xyz" does not.
"""
def xyz_there(str):
    array = str.split('.xyz')
    for i in array:
        if i.find('xyz') >= 0:
            return True
    return False