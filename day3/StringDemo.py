# create string variable
# ways of creating string variables
# S = "welcome"
# s = 'welcome'
# s = str('welcome')
# s = str("welcome")
# creation empty string variables
# name = ""
# name = ''
# name = str()
# mutable- cannot change the value of the variable.
# immutable - can change the value of variable.
# string is immutable
# str1 = "welcome"
# print(id(str1))

# str1 = "welcome"
# print(id(str1))  # 2984541559472
# print(str1)
# str1 = str1 + "to python"
# print(id(str1))  # 1638475397872
# print(str1)
# if the value is changed after updation then it is immutable

# Example 3 : + and * with string
# str="welcome"
# print(str+"programming")
# print(str×3) #welcomewelcomewelcome
# concatenation/joining


# Example4 = Slicing  []
# starting index 0
# ending index 1
# str = "welcome"
# print(str[1:3])  # el
# print(str[:6])  # welcom here starting index is§o by default
# print(str[2:])  # lcome
#
# print(str[1:-1])  # elcom last 1 char removed
# print(str[1:-2])  # elco last 2 chars removed


# Example5 : ord() and chr()
# print(ord('A'))  # 65 # returns the ASCII code of the character.
# print(chr(65))  # A # returns character represented by an ASCII number

# Example6: max () min() Len()
# print(max("abc"))  # c
# print(min("abc"))  # a
# print(len("welcome"))  # 7

# Example 7: in, not in operators - returns true/false
# s = "welcome"
# print("come" in s)  # True
# print("lome" in s)  # False
#
# print("come" not in s)  # False
# print("lome" not in s)  # True

# Example8: String comparison
# print("tim" == "tie")  # False
# print("free" != "freedom")  # True
# print("arrow" > "aron")  # True
# print("right" >= "left")  # True
# print("teeth" < "tee")  # False
# print("yellow" <= "fellow")  # False
# print("abc" > "")  # True

# Example9 : Testing strings True/False
# s = "welcome to python"
# print(s.isalnum())  # False
# print("Welcome".isalpha())  # True
# print("2012".isdigit())  # True
# print("first Number".isidentifier())  # False
# print(s.islower())  # True
# print("WELCOME".isupper())  # True
# print(" ".isspace())  # True

# Example10: Searching for Substrings
# s = "welcome to python"
# print(s.endswith("thon"))  # True
# print(s.startswith("good"))  # False
# print(s.find("come"))  # 3
# print(s.find("become"))  # -1 not found
# print(s.count("t"))  # 2 #Returns number of occurrences of substring the string

# Example11: Converting String
# s = "String in PYTHON"
# s1 = s.capitalize()
# print(s1)  # String in python
# s2 = s.title()
# print(s2)  # String In Python
# s3 = s.lower()
# print(s3)  # string in python
# s4 = s.upper()
# print(s4)  # STRING IN PYTHON
# s5 = s.swapcase()
# print(s5)  # STRING IN python
# s6 = s.replace("in", "on")
# print(s6)  # String on PYTHON

# Example12: Reverse a string
# Method1
# s = "welcome"
# rev_str = ""
# for i in s:
#     rev_str = i + rev_str  # emoclen
# print("reversed string is:", rev_str)  # emoclew

# Method2
s = "welcome"
rev_str = s[::-1]  # s[0:7:-1]
print(rev_str)  # emoclew
