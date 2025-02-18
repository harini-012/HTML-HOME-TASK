'''Find the Longest Common Prefix in a Tuple of Strings.
Sample input:
Flower
Flow
Flight
Sample Output:
Fl
'''

l=list(input().split())#Flower flow flight
pre=l[0]#Flower
for word in l[1:]:#flow
    new_pre=""
    for i in range(min(len(pre),len(word))):#min(6,4)
        if pre[i]==word[i]:#f==f
            new_pre+=pre[i]
        else:
            break
    pre=new_pre
    if not pre:
        break
print(pre)


'''2. Create a program that models a Person class and a Student class that inherits from Person.
Base Class (Person):
The Person class defines the basic attributes of a person (name and age) and a method
display_info() to display these details.
Derived Class (Student):
The Student class inherits from Person and adds two new attributes: student_id and course.
It also overrides the display_info() method to include these new attributes while still calling
the base class display_info() method using super().
Object Creation and Method Calls:
• person1 is an instance of the Person class and only displays the name and age.
• student1 is an instance of the Student class, which also displays the student's name, age,
student ID, and course'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Student(Person):
    def __init__(self,name,age,stu_id,course):
        super().__init__(name,age)
        self.stu_id=stu_id
        self.course=course
    def display_info(self):
        super().display_info()
        print("Student id:",stu_id)
        print("Course:",course)
name=input("Enter the name")
age=int(input("Enter the age"))
stu_id=input("Enter the student id")
course=input("Enter the course")
p1=Person(name,age)
p1.display_info()
s1=Student(name,age,stu_id,course)
s1.display_info()



