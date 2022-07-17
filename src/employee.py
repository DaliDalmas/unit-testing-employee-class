from datetime import datetime


class Employee:
    """
    """

    MIN_SALARY: int = 3000

    def __init__(self, first_name: str, middle_name: str, sur_name: str, initial_salary: int, dob: str):
        """
        """
        self.first_name: str = first_name
        self.middle_name: str = middle_name
        self.sur_name: str = sur_name
        self._salary: int = initial_salary
        self._date_of_birth: str = dob

    def __str__(self):
        return f"""
        Employee
        ___________________________
        First name: {self.first_name}
        Middle name: {self.middle_name}
        Sur name: {self.sur_name}
        salary: {self._salary}
        Date of Births: {self._date_of_birth}
        __________________________
        """

    def __repr__(self):
        return(f'Employee("{self.first_name}",\
            "{self.middle_name}",\
            "{self.sur_name}",\
            {self._salary},\
            {self._date_of_birth})')

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, initial_salary: int):
        if initial_salary < Employee.MIN_SALARY:
            raise Exception("Salary less than minimum salary")
        self._salary = initial_salary

    def increase_salary(self, increment: float):
        return self._salary*((100+increment)/100)

    def get_age(self):
        return datetime.today().year - datetime.strptime(
                                        self._date_of_birth,
                                        '%Y-%M-%d').date().year


def main():
    print("Example employee class")
    emp: Employee = Employee("Dalmas", "DaliCodes", "Otieno", 6000, "1992-03-23")
    print(emp)
    print(f"The age of employee is {emp.get_age()}")


if __name__ == "__main__":
    main()
