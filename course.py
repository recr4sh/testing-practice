class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
    
    def update_progress(self, percentage):
        if 0 <= percentage <= 100:
            self.progress = percentage
            return True
        return False
    
    def get_progress(self):
        return self.progress


class Course:
    def __init__(self, title):
        self.title = title
        self.students = []
    
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            return True
        return False
    
    def get_student_count(self):
        return len(self.students)
    
    def get_title(self):
        return self.title
# Updated
