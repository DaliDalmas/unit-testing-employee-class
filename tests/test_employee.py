import pytest
from src import employee


class TestEmployeeObjectCreation:

    def test_employee_object_creation_on_negative_salary(self):
        with pytest.raises(ValueError):
            emp = employee.Employee('Anna', 'Mary', 'Nakato', -20000, '1995-07-17')

    def test_employee_object_creation_on_salary_equals_zero(self):
        with pytest.raises(ValueError):
            emp = employee.Employee('Anna', 'Mary', 'Nakato', 0, '1995-07-17')

    def test_employee_object_creation_on_salary_less_than_min_salary(self):
        with pytest.raises(ValueError):
            emp = employee.Employee('Anna', 'Mary', 'Nakato', 2980, '1995-07-17')

    def test_employee_object_creation_on_wrong_argument_types(self):
        pass

    def test_employee_object_creation_on_missing_arguments(self):
        pass

    def test_employee_object_creation_on_proper_arguments(self):
        pass

    def test_employee_object_creation_on_age_less_than_18(self):
        pass

    def test_employee_object_creation_on_age_greater_than_78(self):
        pass


class TestIncreaseSalary:

    def test_increase_salary_on_increment_greater_than_100(self):
        pass

    def test_increase_salary_on_increment_less_than_0(self):
        pass

    def test_increase_salary_on_increment_equal_to_5(self):
        pass

    def test_increase_salary_on_increment_equal_to_0(self):
        pass

    def test_increase_salary_on_wrong_argument_types(self):
        pass

    def test_increase_salary_on_missing_arguments(self0):
        pass

