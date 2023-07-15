import unittest
from student import Student, first_name, last_name


class TestStudents(unittest.TestCase):

    def test_full_name(self):
        student = Student(first_name, last_name)
        self.assertEqual(student.full_name, "Frank Arellano")

    def test_alert_sante(self):
        student = Student(first_name, last_name)
        student.alert_santa()
        self.assertTrue(student.naughty_list)

    def test_email_address(self):
        student = Student(first_name, last_name)
        self.assertEqual(
            student.get_email, f'{first_name}.{last_name}@mail.com'.lower())


if __name__ == "__main__":
    unittest.main()
