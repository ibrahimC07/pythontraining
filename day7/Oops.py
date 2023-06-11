# Example1

# class MyClass:
#     def myfun(self):
#         pass
#
#     def display(self, name):
#         print(name)
#
#
# mc1 = MyClass()
# mc1.myfun()
# mc1.display("scott")

# Example2:
# class MyClass:
#     def m1(self):
#         print("this is instance method...")
#
#     @staticmethod
#     def m2(self, num):
#         print(self, num)
#
#
# MyClass().m1()
# MyClass().m2(100, 200)

# Example3 :
# class MyClass:
#     a, b = 10, 20  # class variables
#
#     def add(self):
#         print(self.a + self.b)
#
#     def mul(self):
#         print(self.a * self.b)
#
#
# MyClass().add()
# MyClass().mul()

# Example4 :
# i, j = 15, 25  # Global variables
#
#
# class MyClass:
#     a, b = 10, 20  # Class variables
#
#     def add(self, x, y):  # Local variables
#         print(x + y)  # x, y are local variables
#         print(self.a + self.b)  # a, b are class variables
#         print(i + j)  # i, j are global variables
#
#
# MyClass().add(100, 200)

# Example5 :
# a, b = 15, 25  # Global variables
#
#
# class MyClass:
#     a, b = 10, 20  # Class variables
#
#     def add(self, a, b):  # Local variables
#         print(a + b)  # local
#         print(self.a + self.b)  # class
#         print(globals()['a'] + globals()['b'])  # global
#
#
# MyClass().add(100, 200)

# Example: once class can have multiple objects
# class MyClass:
#     def display(self, name):
#         print("this is display method....")
#         print(name)
#
#
# obj1 = MyClass()
# obj1.display("john")
# obj2 = MyClass()
# obj2.display("scott")

# Example7 : Constructor Example
# class MyClass:
#     def __init__(self):
#         print("this is constructor..")
#
#     def m1(self):
#         print("hello...")
#
#     def m2(self, x, y):
#         return (x + y)
#
#
# mc = MyClass()  # invoke constructor automatically
# mc.m1()  # method we have call explicitly by using object
# print(mc.m2(10, 20))

# Example8
# class MyClass:
#     name = "john"
#
#     def __init__(self, name):
#         print(name)
#         print(self.name)
#
#
# # constructor expecting one argument
# mc = MyClass("David")  # passing parameter to the constructor

# Example9
# Req: Emp
# constructor : eid, ename, sal
# display() : print eid, ename & sal
#
# class Emp:
#     def __init__(self, eid, ename, sal):
#         self.eid = eid
#         self.ename = ename
#         self.sal = sal
#
#     def display(self):
#         print(self.eid, self.ename, self.sal)
#
#
# e1 = Emp(101, "john", 500000)
# e1.display()
#
# e2 = Emp(102, "johny", 1500000)
# e2.display()

# Example10 # in this example the __str__ returns only strings arguments
# Reg: Emp
# constructor : eid, ename, sal
# constructor: print eid, ename & sal
# class Emp:
#     def __init__(self, eid, ename, sal):
#         self.eid = eid
#         self.ename = ename
#         self.sal = sal
#
#     def __str__(self):
#         return (self.ename)
#
#
# e1 = Emp(101, "john", 500000)
# print(e1)
