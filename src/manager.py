from employee import Employee


from employee import Employee

class Manager(Employee):

    def __init__(self, first_name, middle_name, sur_name, initial_salary, dob, role="manager", percentage_increment=5, team="admin"):
        self.role = role
        self._salary_percentage_increment = percentage_increment
        self.my_budget_stats = None

        Employee.__init__(self, first_name, middle_name, sur_name, initial_salary, dob)
        self._salary = Employee.increase_salary()

    @property
    def salary_percentage_increment(self):
        return self._salary_percentage_increment

    @property.setter
    def salary_percentage_increment(self, percentage_increment):
        if percentage_increment<0:
            raise Exception("Invalid salary increment")
        self._salary_percentage_increment = percentage_increment

    def create_budgegt_stats(self, prev_budget, prev_funding, prev_expenditure, next_budget, next_funding):

        self.my_budget_stats = {
            "prev_budget": prev_budget,
            "prev_funding": prev_funding,
            "prev_expenditure": prev_expenditure,
            "next_budget": next_budget,
            "next_funding": next_funding,
            "budge_percentage_change": (prev_budget-next_budget)*100/prev_budget,
            "prev_budget_percentage_not_funded": (prev_budget-prev_funding)*100/prev_budget,
            "percentage_surplus_funding": (prev_funding-prev_expenditure)*100/prev_funding,
            "funding_percentage_change": (prev_funding-next_funding)*100/prev_funding
        }

        return self.my_budget_stats