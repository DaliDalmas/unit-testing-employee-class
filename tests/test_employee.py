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
        # test first name on type not string
        with pytest.raises(TypeError):
            emp = employee.Employee(10, 'Mary', 'Nakato', 10000, '1995-07-17')
        # test middle name on type not string
        with pytest.raises(TypeError):
            emp = employee.Employee('Anna', 909, 'Nakato', 10000, '1995-07-17')
        # test last name on type not string
        with pytest.raises(TypeError):
            emp = employee.Employee('Anna', 'Mary', 98, 10000, '1995-07-17')
        # test salary on type not int or float
        with pytest.raises(TypeError):
            emp = employee.Employee('Anna', 'Mary', 'Nakato', '10000', '1995-07-17')
        # test date on type not string
        with pytest.raises(TypeError):
            emp = employee.Employee('Anna', 'Mary', 'Nakato', 10000, 1995)

    def test_employee_object_creation_on_proper_arguments(self):
        emp = employee.Employee('Anna', 'Mary', 'Nakato', 4000, '1995-07-17')
        assert emp.first_name == 'Anna'
        assert emp.middle_name == 'Mary'
        assert emp.sur_name == 'Nakato'
        assert emp._salary == 4000
        assert emp._date_of_birth == '1995-07-17'

    def test_employee_object_creation_on_age_less_than_18(self):
        with pytest.raises(AttributeError):
            emp = employee.Employee('Anna', 'Mary', 'Nakato', 4000, '2015-07-17')
        

    def test_employee_object_creation_on_age_greater_than_78(self):
        with pytest.raises(AttributeError):
            emp = employee.Employee('Anna', 'Mary', 'Nakato', 4000, '1940-07-17')


class TestIncreaseSalary:

    def test_increase_salary_on_increment_greater_than_100(self):
        emp = employee.Employee('Anna', 'Mary', 'Nakato', 10000, '1995-07-17')
        assert emp.increase_salary(110)==20000

    def test_increase_salary_on_increment_less_than_0(self):
        emp = employee.Employee('Anna', 'Mary', 'Nakato', 10000, '1995-07-17')
        with pytest.raises(AttributeError):
            emp.increase_salary(-10)

    def test_increase_salary_on_increment_less_than_minimum_increment(self):
        emp = employee.Employee('Anna', 'Mary', 'Nakato', 10000, '1995-07-17')
        with pytest.raises(AttributeError):
            emp.increase_salary(4)

    def test_increase_salary_on_wrong_argument_types(self):
        emp = employee.Employee('Anna', 'Mary', 'Nakato', 10000, '1995-07-17')
        with pytest.raises(ValueError):
            emp.increase_salary('something')

