import unittest
from student import Student, first_name, last_name, student_extension
from datetime import timedelta


class TestStudents(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('OPEN - setUpClass')
        cls.student = Student(first_name, last_name)

    @classmethod
    def tearDownClass(cls):
        print('CLOSE - tearDownClass')

    # def setUp(self):
    #     print('\nOPEN TEST - self.student')
    #     self.student = Student(first_name, last_name)

    # def tearDown(self):
    #     print('CLOSE TEST - self.student')

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, "Frank Arellano")

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email_address(self):
        print('test_email_address')
        self.assertEqual(
            self.student.get_email,
            f'{first_name}.{last_name}@mail.com'.lower())

    def test_apply_extension(self):
        print('test_apply_extension')
        old_date = self.student.end_date
        self.student.apply_extension(student_extension)
        self.assertNotEqual(self.student.end_date, old_date)


if __name__ == "__main__":
    unittest.main()
