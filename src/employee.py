from datetime import datetime 
class Employee:
    """
    """
    MIN_SALARY = 3000
    def __init__(self, first_name, middle_name, sur_name, initial_salary, dob):
        """
        """
        self.first_name = first_name
        self.middle_name = middle_name
        self.sur_name = sur_name
        self._salary = initial_salary
        self._date_of_birth = dob

    def __str__(self):
        return f"""
        Employee
        ___________________________
        First name: {self.first_name}
        Middle name: {self.middle_name}
        Sur name: {self.sur_name}
        salary: {self._salary}
        """
    def __repr__(self):
        return(f'Employee("{self.first_name}", "{self.middle_name}", "{self.sur_name}", {self._salary})')

    @property
    def salary(self):
        return self._salary

    @property.setter
    def salary(self,initial_salary):
        if initial_salary<Employee.MIN_SALARY:
            raise Exception("Salary less than minimum salary")
        self._salary = initial_salary

    @classmethod
    def increase_salary(cls):
        return cls._salary*((100+cls._salary_percentage_increment)/100)

    def get_age(self):
        return datetime.now - self._date_of_birth
