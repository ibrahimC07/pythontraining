# Example1
# print("this is starting point of program..")
# print("this is starting point of program...")
# print("this is starting point of program.")
# try:
#     print(x)
# except:
#     print("Exception occured")
# print("this is end of the program..")
# print("this is end of the program.")
# print("this is end of the program.")

# # Example2
# print("this is starting point of program..")
# print("this is starting point of program...")
# try:
#     print(10 / 0)
# except:
#     print("Exception occured...handled")
# print("program completed ...")

# Example3 : Multiple except blocks  - try, exept else, finally
# try:
#     num1, num2 = 10, 0
#     result = num1 / num2
#     print("result is:", result)
# except ZeroDivisionError:
#     print("Thrown ZeroDivisionError exception...")
# except SyntaxError:
#     print("Thrown Syntax error exception...")
# except:
#     print("Exception handled...")
# else:
#     print("No exception occured...")
# finally:
#     print("always execut...")

# Example4 : raising our own exceptions
def enterage(num):
    if num < 0:
        raise ValueError("Only integers are allowed")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


enterage(10)
enterage(5)
num = -1
try:
    enterage(num)
except ValueError:
    print("value error exception occured and handled...")
