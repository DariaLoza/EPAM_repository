from homeworks.homework11.task1 import SimplifiedEnum


def test_metaclass_simplified_sets_colors_enum_attrs_in__keys():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.BLACK == "BLACK"


def test_metaclass_simplified_sets_size_enum_attrs_in__keys():
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert SizesEnum.XL == "XL"
    assert SizesEnum.XS == "XS"
