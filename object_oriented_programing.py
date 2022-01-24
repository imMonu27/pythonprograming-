# a class is a blueprint for creating object
'''class Number:
    def sum(self):
        return self.a+self.b
num=Number()
num.a=12
num.b=13
s=num.sum()
print(s)'''


# object:
# an object is an insertion of a class.

'''class Railwayform:
    formtype="railwayform"
    def printData(self):
        print(f"name is {self.name}")
        print(f"train is {self.train}")
mohitapplication=Railwayform()
mohitapplication.name="mohit"
mohitapplication.train="rajdhani"
mohitapplication.printData()'''

# modeling python in oops!
'''
noun - class - Employee
adjective - attributes - name,age,salery
verds - methods - getsalary(),increment()
'''

# class atrributes
# an atrributes that belongs to the class rether than particular object
class Employee:
    company="google"
mohit=Employee()

mohit.company
Employee.company="youtube"
print()
