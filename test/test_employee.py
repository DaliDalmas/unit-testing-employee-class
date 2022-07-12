import pytest
from employee import Employee

class TestSalaryIncrement:
    @pytest.xfail
    def test_salary_increment_on_negative_increment():
        pass