from datetime import date, timedelta


class Student:
    """ This is a class for method testins"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_Date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f'{self._first_name} {self._last_name}'

    @property
    def get_email(self):
        return f'{self._first_name}.{self._last_name}@mail.com'.lower()

    def alert_santa(self):
        self.naughty_list = True


first_name = input('Student First Name: ')
last_name = input('Student Last Name: ')

if __name__ == "__main__":
    student = Student(first_name, last_name)
    print(student.full_name)