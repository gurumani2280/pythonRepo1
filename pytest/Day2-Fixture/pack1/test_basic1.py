import pytest


def test_basic1(setup):
    print("This is first pytest program")
def test_basic3():
    print("This is third pytest program")
@pytest.fixture
def setup():
    print(" this is setup runs before method")
    yield
    print("this is tear down method which executes after setup")
