from ex3_2 import Student
from ex3_1 import CourseGroup

student = Student("Иван", "Иванов", 30, "Инженер по тестированию")
classmate1 = Student("Петр", "Петров", 35, "Инженер по тестированию")
classmate2 = Student("Семен", "СидороваСеменов", 25, "Инженер по тестированию")
classmate3 = Student("Федор", "Федоров", 20, "Инженер по тестированию")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])

print(course_group)
