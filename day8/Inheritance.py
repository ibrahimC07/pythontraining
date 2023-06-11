# Example1
# class A:
#     def m1(self):
#         print("this is m1 method from class A")
#
#
# class B(A):
#     def m2(self):
#         print("this is m2 method from class B")
#
#
# bobj = B()
# bobj.m1()  # this is m1 method from class A
# bobj.m2()  # this is m2 method from class B

# Example2 : single inheritance
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 200, 100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# bobj = B()
# bobj.m1()
# bobj.m2()

# Example3 : Multilevel inheritance
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 200, 100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(B):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
#
# cobj = C()
# cobj.m1()
# cobj.m2()
# cobj.m3()


# Example4 : Hierarchy inheritance
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 200, 100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(A):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
#
# bobj = B()
# bobj.m1()
# bobj.m2()
# cobj = C()
# cobj.m1()
# cobj.m3()

# Example5 : Multiple inheritance
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B:
#     a, b = 200, 100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# class C(A, B):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
#
# cobj = C()
# cobj.m1()
# cobj.m2()
# cobj.m3()

# Example:  calling parent class method using child class (super())
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
#
#
# class B(A):
#     def m1(self):
#         print("This is m1 method from class B")
#         super().m1()
#
#
# bobj = B()
# bobj.m1()
#
#
# # Example7
# class A:
#     a, b = 10, 20
#
#
# class B(A):
#     i, j = 100, 200
#
#     def m(self, x, y):
#         print(x + y)  # local variables
#         print(self.i + self.j)  # class vardibles
#         print(self.a + self.b)  # class variables
#
#
# bobj = B()
# bobj.m(1000, 2000)

# Example8: overriding variables
# class Parent:
#     name = "Scott"
#
#
# class Child(Parent):
#     name = "John"  # overriding the variable value
#     def test(self):
#         print(super().name)
#
#
# cobj = Child()
# print(cobj.name)
# cobj.test()

# Example9 : Overriding Methods
# class Bank:
#     def rate0fInterest(self):
#         return 0
#
#
# class XBank(Bank):
#     def rate0fInterest(self):
#         return 10
#
#
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 13
#
#
# objx = XBank()
# print(objx.rate0fInterest())  # 10
# objy = YBank()
# print(objy.rateOfInterest())
# Example10: overloading (polymorphism)
# class Human:
#     def sayhello(self, name=None):
#         if name is not None:
#             print("Hello" + name)
#         else:
#             print("Hello")
#
#
# h = Human()
# h.sayhello("scott")
# h.sayhello()
#
# # Example11: overloading 2
# class Calculation:
#     def add(self,a=0,b=0,c=0):
#         print(a+b+c)

#
# calobj=Calculation()
# calobj.add()
# calobj.add(10,20)
# calobj.add(100,200,300)