import pytest
from addition.simple import add


def test_zero_addition():
    assert add(0, 0) == 0


def test_identity_add():
    assert add(0, 1) == 1
    assert add(1, 0) == 1


@pytest.mark.parametrize("test_input,expected", [
    ((1, 1), 2),
    ((1, 2), 3),
    ((2, 1), 3),
    ((3, 3), 6),
    ((1, 4), 5)
])
def test_multi_slaps(test_input, expected):
    assert add(*test_input) == expected


@pytest.mark.skip(reason="negative numbers not supported yet")
def test_regex_slaps():
    assert add(-1, -1) == -2


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


def test_invalid_slap():
    with pytest.raises(TypeError):
        add(1, None)


@pytest.mark.xfail
def test_db_slap(db_conn):
    db_conn.read_slaps()
    assert ...


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"
