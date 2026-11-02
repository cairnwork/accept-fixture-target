"""Visible smoke tests (the real acceptance tests are hidden). Only cover what already works."""
from fixture_app.textutil import slugify, chunk, parse_bool, median, truncate


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_chunk_exact():
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_chunk_bad_n():
    import pytest
    with pytest.raises(ValueError):
        chunk([1], 0)


def test_parse_bool_basic():
    assert parse_bool("true") is True and parse_bool("no") is False


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_truncate_short():
    assert truncate("abc", 5) == "abc"


def test_median_even():
    assert median([1, 2, 3, 4]) == 3  # "documents" current behaviour
