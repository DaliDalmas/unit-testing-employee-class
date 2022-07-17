from employee import Employee


class Manager(Employee):

    def __init__(self, first_name, middle_name, sur_name, initial_salary, dob,
                 role="manager", percentage_increment=5, team="admin"):
        self.role = role
        self._salary_percentage_increment = percentage_increment
        self.team = team
        self.my_budget_stats = None

        Employee.__init__(
            self,
            first_name,
            middle_name,
            sur_name,
            initial_salary,
            dob)
        self._salary = Employee.increase_salary(self)

    @property
    def salary_percentage_increment(self):
        return self._salary_percentage_increment

    @salary_percentage_increment.setter
    def salary_percentage_increment(self, percentage_increment):
        if percentage_increment < 0:
            raise Exception("Invalid salary increment")
        self._salary_percentage_increment = percentage_increment

    def create_budgegt_stats(
            self,
            prev_budget,
            prev_funding,
            prev_expenditure,
            next_budget,
            next_funding):

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
    emp = Manager(
        "Dalmas", "DaliCodes", "Otieno",
        6000, "1992-03-23", "CTO", 50,
        "Technology")

    print(emp)
    print(f"The age of employee is {emp.get_age()}")


if __name__ == "__main__":
    main()
