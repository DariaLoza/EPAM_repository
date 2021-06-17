from homeworks.homework6.task1 import User, Vehicle


def test_first_user():
    assert User.get_created_instances() == 0
    user_1, _, _ = User(), User(), User()
    assert user_1.get_created_instances() == 3
    assert user_1.reset_instances_counter() == 3


def test_class_Vehicle():
    assert Vehicle.get_created_instances() == 0
    Vehicle_1, _, _ = User(), User(), User()
    assert Vehicle_1.get_created_instances() == 3
    assert Vehicle_1.reset_instances_counter() == 3
