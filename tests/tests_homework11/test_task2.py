from homeworks.homework11.task2 import Order, elder_discount, morning_discount


def test_Order_class_with_morning_discount():
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50


def test_Order_class_with_elder_discount():
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10
