"""Vacation accounting system"""


class Employee:
    """The object of the class is an employee of the company"""
    vacation_days = 28

    def __init__(self, first_name: str, second_name: str, gender: str):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days
        self._employee_id = self.__generate_employee_id()

    def __generate_employee_id(self):
        """The method returns the hash-value of string"""
        return hash(self.first_name +
                    self.second_name +
                    self.gender)

    def consume_vacation(self, spent_vacations_days: int):
        """ The method takes into account
           the remaining days of the employee's vacation"""

        self.remaining_vacation_days -= spent_vacations_days

    def get_vacation_details(self):
        """The method returns the number
           of remaining vacation days of the employee"""

        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

    def __str__(self):
        return 'The object of the class is an employee of a company!'


class FullTimeEmployee(Employee):
    """The object of the class is a full-time employee"""

    def __init__(self, first_name: str,
                 second_name: str, gender: str, __salary: int):
        self.__salary = __salary
        super().__init__(first_name, second_name, gender)

    def __get_vacation_salary(self):
        """The method returns the amount of vacation pay"""

        return 0.8 * self.__salary
    unused_value = __get_vacation_salary

    def get_unpaid_vacation(self,
                            start_vacation_date: str,
                            amount_of_unpaid_vacation_days: int):
        """The method returns the beginning
           and duration of unpaid vacation"""

        return (f'Начало неоплачиваемого отпуска: {start_vacation_date}, '
                f'продолжительность: {amount_of_unpaid_vacation_days} дней.')


class PartTimeEmployee(Employee):
    """The object of the class is a part-time employee"""

    vacation_days = 14

    def __init__(self, first_name: str, second_name: str, gender: str):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days


full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))

part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')
part_time_employee.consume_vacation(5)
print(part_time_employee.get_vacation_details())
