from app.script.onsite import foo


def test_foo():
    bar = foo(1)
    assert bar == 1
