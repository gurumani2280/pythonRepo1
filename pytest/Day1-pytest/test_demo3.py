import pytest


def f():
    raise SystemExit(1)
    #pass     #E  Failed: DID NOT RAISE <class 'SystemExit'>


def test_mytest():
    with pytest.raises(SystemExit):
        f()

def test_mytest2():
    f()

