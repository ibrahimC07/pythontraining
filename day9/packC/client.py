import sys
sys.path.append("C:/Users/admin/PycharmProjects/Pythontraining/day9/packA")
sys.path.append("C:/Users/admin/PycharmProjects/Pythontraining/day9/packB")

#Appraoch1
# import emp
# empobj=emp.Employee(101,"JOHN",500000)
# empobj.displayemp()
#
# import stu
# stuobj=stu.Student(1122,"scott",'B')
# stuobj.displaystu()

#Appraoch2
from emp import Employee
empobj=Employee(101,"JOHN",500000)
empobj.displayemp()

from stu import Student
stuobj=Student(1010,"David",500000)
stuobj.displaystu()