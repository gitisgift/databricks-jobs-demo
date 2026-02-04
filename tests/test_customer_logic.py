import pytest
from src.jobs.logic import generate_rows


def test_generate_rows_basic():
    rows = generate_rows(3, "api")

    assert rows == [
        (0, "api"),
        (1, "api"),
        (2, "api"),
    ]


def test_generate_rows_zero():
    rows = generate_rows(0, "x")
    assert rows == []


def test_generate_rows_negative_limit():
    with pytest.raises(ValueError):
        generate_rows(-1, "bad")
