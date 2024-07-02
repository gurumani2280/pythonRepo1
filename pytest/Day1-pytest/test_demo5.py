import pytest


class TestClassDemoInstance:
    value = 0 #Static variable/ClassVariable

    def test_one(self):
        print()
        print("self.value", self.value) #its just accessing the value and taking static variable
        print("TestClassDemoInstance.value", TestClassDemoInstance.value)
        self.value = 1 #Due to =operator, it will create a new instance variable with name as value.And its value=1
        print()
        print("self.value", self.value) #After line8, this is accessing as instance variable and no more accessing the static variable
        print("TestClassDemoInstance.value", TestClassDemoInstance.value)
        assert self.value == 1

    @pytest.mark.regression
    def test_two(self):
        print()
        print("in test_two method self.value", self.value)
        assert self.value == 1 #It is double= ,so not assignment operator