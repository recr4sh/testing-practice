import unittest
from course import Course, Student


class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        """Test student creation"""
        student = Student("Ivan Ivanov")
        self.assertEqual(student.name, "Ivan Ivanov")
        self.assertEqual(student.progress, 0)
    
    def test_update_progress(self):
        """Test progress update"""
        student = Student("Maria")
        result = student.update_progress(75)
        self.assertTrue(result)
        self.assertEqual(student.get_progress(), 75)
    
    def test_invalid_progress(self):
        """Test invalid progress value"""
        student = Student("Petr")
        result = student.update_progress(150)
        self.assertFalse(result)
        self.assertEqual(student.get_progress(), 0)


class TestCourse(unittest.TestCase):
    def test_course_creation(self):
        """Test course creation"""
        course = Course("Python for Beginners")
        self.assertEqual(course.get_title(), "Python for Beginners")
        self.assertEqual(course.get_student_count(), 0)
    
    def test_add_student(self):
        """Test adding student"""
        course = Course("Web Development")
        student = Student("Anna")
        result = course.add_student(student)
        self.assertTrue(result)
        self.assertEqual(course.get_student_count(), 1)
    
    def test_duplicate_student(self):
        """Test adding duplicate student"""
        course = Course("Databases")
        student = Student("Sergey")
        course.add_student(student)
        result = course.add_student(student)
        self.assertFalse(result)
        self.assertEqual(course.get_student_count(), 1)


if __name__ == '__main__':
    unittest.main()
