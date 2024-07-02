import pytest


@pytest.mark.webtest
def test_send_http():
    print("This is test_send_http")

@pytest.mark.regression
def test_something_quick():
    print("This is test_something_quick")


def test_another():
    print("This is test_another")



class TestClass2:
    def test_method2(self):
        print("This is test_method2")