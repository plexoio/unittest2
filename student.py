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

    def apply_extension(self, student_extension):
        old_date = self.end_date
        self.end_date = self.end_date + timedelta(days=student_extension)
        return f'End: {old_date} || End: {self.end_date}'


print('Check In Student\n')
first_name = input('First Name: ')
last_name = input('Last Name: ')
check_extension = input('Student Extension? N/Y: ')

if check_extension.lower() == "y":
    student_extension = int(input("Introduce days: "))
else:
    student_extension = 0
    print('No changes were made!')

if __name__ == "__main__":
    student = Student(first_name, last_name)
    print(student.full_name, ' | ', student.apply_extension(student_extension))
