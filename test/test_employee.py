import pytest
from ..src.employee import Employee


class TestEmployeeObjectCreation:

    def test_employee_object_creation_on_negative_salary(self):
        pass

    def test_employee_object_creation_on_salary_equals_zero(self):
        pass

    def test_employee_object_creation_on_salary_less_than_min_salary(self):
        pass

    def test_employee_object_creation_on_none_integer_salary(self):
        pass

    def test_employee_object_creation_on_missing_arguments(self):
        pass

    def test_employee_object_creation_on_proper_arguments(self):
        pass

    def test_employee_object_creation_on_none_date_string(self):
        pass

    def test_employee_object_creation_on_age_less_than_18(self):
        pass

    def test_employee_object_creation_on_age_greater_than_78(self):
        pass

    def test_employee_object_creation_on_float_salary(self):
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

    def test_increase_salary_on_float_value_increment(self):
        pass

    def test_increase_salary_on_str_value_increment(self):
        pass

    def test_increase_salary_on_missing_arguments(self0):
        pass
