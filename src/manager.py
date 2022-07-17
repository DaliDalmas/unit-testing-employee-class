from employee import Employee


class Manager(Employee):

    def __init__(self, first_name: str, middle_name: str, sur_name: str, initial_salary: int, dob: str,
                 role :str="manager", percentage_increment:int=5, team:str="admin"):
        self.role: str= role
        self._salary_percentage_increment: str = percentage_increment
        self.team: str = team
        self.my_budget_stats: dict = {}

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

    def create_budget_stats(
            self,
            prev_budget: float,
            prev_funding: float,
            prev_expenditure: float,
            next_budget: float,
            next_funding: float):

        self.my_budget_stats = {
            "prev_budget": prev_budget,
            "prev_funding": prev_funding,
            "prev_expenditure": prev_expenditure,
            "next_budget": next_budget,
            "next_funding": next_funding,
            "budge_percentage_change":
            (prev_budget-next_budget)*100/prev_budget,
            "prev_budget_percentage_not_funded":
            (prev_budget-prev_funding)*100/prev_budget,
            "percentage_surplus_funding":
            (prev_funding-prev_expenditure)*100/prev_funding,
            "funding_percentage_change":
            (prev_funding-next_funding)*100/prev_funding
        }

        return self.my_budget_stats

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

    print("Creating budget statistics")
    print(emp.create_budget_stats(20000, 19000, 14569, 30000, 23140))


if __name__ == "__main__":
    main()
