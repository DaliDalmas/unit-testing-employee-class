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
        Date of Births: {self._date_of_birth}
        __________________________
        """

    def __repr__(self):
        return(f'Employee("{self.first_name}", "{self.middle_name}", "{self.sur_name}", {self._salary}, {self._date_of_birth})')

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,initial_salary):
        if initial_salary < Employee.MIN_SALARY:
            raise Exception("Salary less than minimum salary")
        self._salary = initial_salary

    def increase_salary(self):
        return self._salary*((100+self._salary_percentage_increment)/100)

    def get_age(self):
        return datetime.today().year - datetime.strptime(self._date_of_birth, '%Y-%M-%d').date().year

def main():
    print("Example employee class")
    emp = Employee("Dalmas", "DaliCodes", "Otieno", 6000, "1992-03-23")
    print(emp)
    print(f"The age of employee is {emp.get_age()}")

if __name__=="__main__":
    main()