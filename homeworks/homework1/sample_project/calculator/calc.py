def check_power_of_2(a: int) -> bool:
    """This check if the integer is power of 2"""
    return not (bool(a & (a - 1))) if a != 0 else False
