import unittest
from student import Student, first_name, last_name


class TestStudents(unittest.TestCase):

    # Before and after all test cases
    @classmethod
    def setUpClass(cls):
        print('OPEN - setUpClass')
        cls.student = Student(first_name, last_name)

    @classmethod
    def tearDownClass(cls):
        print('CLOSE - tearDownClass')

    # Before and after each test case
    def setUp(self):
        print('\nOPEN TEST - self.student')
        self.student = Student(first_name, last_name)

    def tearDown(self):
        print('CLOSE TEST - self.student')

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


if __name__ == "__main__":
    unittest.main()
