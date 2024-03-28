"""
STUDENT.PY
THIS IS A FILE THAT HOLDS TWO CLASSES
"""

import random

class Student:

    '''
    THIS IS A PARENT CLASS
    '''
    def __init__(self, name, major, progress, study_time):
        self.name = name
        self.major = major #The student's choice of major and study
        self.progress = progress #The student's progress in the major
        self.study_time = study_time #Time spent studying in hours

    def study_more(self, amount):
        '''
        This method keeps track of the time the student spends studying
        '''
        self.study_time += amount #Adds additional time to the study_time
        self.progress_status() #To update the progress status
                                      #Based on amount of time spent studying
        return f"{self.name} has studied an additional {amount} hours of studying this week" #Returns the value of hours spent studying
    
    def progress_status(self):
        '''
        This method updates the progress status based on the time spent studying
        '''
        if self.study_time <= 20:
            self.progress = 'Beginner' #Threshold to reach before progressing
        elif 21 <= self.study_time <= 50:
            self.progress = 'Intermediate' #Threshold to reach before progressing
        else:
            self.progress = 'Expert' #Benchmark for acheiving Expert status
        return f"{self.name}'s is at a(n) {self.progress} level, after studying {self.study_time} hours"
    
    def __repr__(self):
        return f"{self.name} is a(n) {self.progress} {self.major} major"

# if __name__ == '__main__': #James
#     student1 = Student('James', 'Art', 'Beginner', 5)
    
#     print(f"Name: {student1.name}")
#     print(f"Major: {student1.major}")
#     print(f"Study Hours: {student1.study_time}")

#     print(student1.study_more(16))
#     print(student1.progress_status())
#     print(student1.__repr__)
    
class BloomtechStudent(Student):
    '''
    THIS IS A CHILD CLASS
    '''
    def __init__(self, name, major, progress, study_time, num_prog):
        super().__init__(name, major, progress, study_time)
        self.num_prog = num_prog
    
    def bld_prog(self, amount):
        '''
        This method adds to the 'num_prog' count
        '''
        self.num_prog += amount
        return self.num_prog

# if __name__ == '__main__': #Dallin
#     student2 = BloomtechStudent('Dallin', 'Data-Science', 'Beginner', 25, 3)

#     print(f"Name: {student2.name}")
#     print(f"Major: {student2.major}")
#     print(f"Study Hours: {student2.study_time}")

#     print(student2.study_more(20))
#     print(student2.progress_status())
#     print(student2.bld_prog(3))
#     print(student2.__repr__)

def student_generator(num_students= 30):
    '''
    This method randomly generates 30 students
    '''

    first_names = ['Arthur', 'Becky', 'Darrell', 'Eric', 'Francine', 'Gary']

    random_first_name = random.choice(first_names)

    random_name = random_first_name

    random_major = random.choice(['Web Development', 'Data Science', 'Backend Development'])

    random_progress = random.choice(['Beginner', 'Intermediate', 'Expert'])

    random_study = random.randint(1, 50)

    random_prog_num = random.randint(1, 10)

    students = []

    for _ in range(num_students):
        students.append(Student(
            random_name, random_major, random_progress, random_study, random_prog_num))

    return students

# print(student_generator(2))
