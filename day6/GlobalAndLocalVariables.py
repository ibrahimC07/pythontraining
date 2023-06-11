# Example1
# global_var = 20
#
#
# # global variable
# def func():
#     local_var = 10  # local variable
#     print(local_var)
#     print(global_var)
#
#
# func()
# # print(local_var) # invalid bcoz local_var is local varaible of func()
# print(global_var)

# Example2:
# xy = 100  # global variable
#
#
# def cool():
#     xy = 200  # Local variable
#
#
# print(xy)
#
# cool()  # 200

# Example3: Using Global variable in local variable and update value
# xy = 100  # global variable
#
#
# def cool():
#     global xy
#     xy = 200  # global variable
#     print(xy)
#
#
#
# cool()  # 200
# print(xy)  # 200

# Example4:
# There is no need to declare global variables outside the function.
# You can declare them global inside the function. - global
def cool():
    global x
    x = 100
    print(x)


cool()
print(x)
