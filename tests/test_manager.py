import pytest
from src import manager


class TestManagerObjectCreation:

    def test_manager_object_creation_on_wrong_argument_types(self):
        # test manager creation on role
        with pytest.raises(TypeError):
            man = manager.Manager('Anna', 'Mary', 'Nakato', 4000, '1995-07-17', 909, 50, 'data')
        # test manager creation on percentage_increment
        with pytest.raises(TypeError):
            man = manager.Manager('Anna', 'Mary', 'Nakato', 4000, '1995-07-17', 'data lead', 'fifty', 'data')
        # test manager creatioin on team
        with pytest.raises(TypeError):
            man = manager.Manager('Anna', 'Mary', 'Nakato', 4000, '1995-07-17', 'data lead', 50, 30)

    def test_manager_object_creation_on_right_argument_types(self):
        # test manager creation on role
        man = manager.Manager('Anna', 'Mary', 'Nakato', 4000, '1995-07-17', 'data lead', 50, 'data')
        assert man.first_name == 'Anna'
        assert man.middle_name == 'Mary'
        assert man.sur_name == 'Nakato'
        assert man._salary == 6000
        assert man._date_of_birth == '1995-07-17'
        assert man.role == 'data lead'
        assert man._salary_percentage_increment == 50
        assert man.team == 'data'