from src.employee import Employee


class Manager(Employee):
    """
    This is a manager class that inherits properties of employee class
    """

    def __init__(self, first_name: str, middle_name: str, sur_name: str, initial_salary: int, dob: str,
                 role :str="manager", percentage_increment:int=5, team:str="admin"):
        self.role: str= role
        self._salary_percentage_increment: str = percentage_increment
        self.team: str = team

        if isinstance(role, str):
            pass
        else:
            raise TypeError("The type of role should be string")
        
        if isinstance(percentage_increment, int):
            pass
        elif isinstance(percentage_increment, float):
            pass
        else:
            raise TypeError("percentage increment should be int or float")

        if isinstance(team, str):
            pass
        else:
            raise TypeError("The type of role should be string")

        Employee.__init__(
            self,
            first_name,
            middle_name,
            sur_name,
            initial_salary,
            dob)

        self._salary = Employee.increase_salary(self, self._salary_percentage_increment)

    @property
    def salary_percentage_increment(self):
        return self._salary_percentage_increment

    @salary_percentage_increment.setter
    def salary_percentage_increment(self, percentage_increment: float):
        if percentage_increment < 0:
            raise Exception("Invalid salary increment")
        self._salary_percentage_increment = percentage_increment

    def __str__(self):
        return f"""
        Employee
        ___________________________
        First name: {self.first_name}
        Middle name: {self.middle_name}
        Sur name: {self.sur_name}
        salary: {self._salary}
        Date of Birth: {self._date_of_birth}
        Role: {self.role}
        team:{self.team}
        __________________________
        """

    def __repr__(self):
        return f'Manager("{self.first_name}",\
            "{self.middle_name}", "{self.sur_name}",\
            {self.salary}, "{self._date_of_birth}",\
            "{self.role}", {self._salary_percentage_increment}, "{self.team}")'


def main():
    print("Example employee class")
    emp: Manager = Manager(
        "Dalmas", "DaliCodes", "Otieno",
        6000, "1992-03-23", "CTO", 50,
        "Technology")

    print(emp)
    print(f"The age of employee is {emp.get_age()}")

if __name__ == "__main__":
    main()
