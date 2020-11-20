
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_number_of_marks(self):
        print(len(self.marks))
    def get_total_sum_of_marks(self):
        print(sum(self.marks))
    def maximum_mark(self):
        print(max(self.marks))
    def minimum_mark(self):
        print(min(self.marks))
    def average_marks(self):
        print(sum(self.marks)/(len(self.marks)))
    def add_mark(self,new_mark):
        self.marks.append(new_mark)
    def remove_mark_at_index(self,index):
        del self.marks[index]


student = Student("juan",[10,8,5,4])

student.get_number_of_marks()

student.get_total_sum_of_marks()

student.maximum_mark()

student.minimum_mark()

student.average_marks()

student.add_mark(11)
student.get_number_of_marks()

print(student.marks[0])
student.remove_mark_at_index(0)

print(student.marks[0])

tuple1 = 1,2,3

print(tuple1)
print(tuple1[0])