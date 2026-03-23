"""Module for online learning system with courses and students."""


class Student:
    """Represents a student in the learning system."""

    MIN_PROGRESS = 0
    MAX_PROGRESS = 100

    def __init__(self, name):
        """
        Initialize a new student.

        Args:
            name (str): Student's name
        """
        self.name = name
        self.progress = self.MIN_PROGRESS

    def update_progress(self, percentage):
        """
        Update student's progress.

        Args:
            percentage (int): Progress percentage (0-100)

        Returns:
            bool: True if update successful, False otherwise
        """
        if self.MIN_PROGRESS <= percentage <= self.MAX_PROGRESS:
            self.progress = percentage
            return True
        return False

    def get_progress(self):
        """
        Get current progress.

        Returns:
            int: Current progress percentage
        """
        return self.progress


class Course:
    """Represents a course in the learning system."""

    def __init__(self, title):
        """
        Initialize a new course.

        Args:
            title (str): Course title
        """
        self.title = title
        self.students = []

    def add_student(self, student):
        """
        Add a student to the course.

        Args:
            student (Student): Student object to add

        Returns:
            bool: True if added successfully, False if duplicate
        """
        if not isinstance(student, Student):
            return False

        if student not in self.students:
            self.students.append(student)
            return True
        return False

    def get_student_count(self):
        """
        Get number of enrolled students.

        Returns:
            int: Number of students
        """
        return len(self.students)

    def get_title(self):
        """
        Get course title.

        Returns:
            str: Course title
        """
        return self.title
