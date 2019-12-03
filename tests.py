import os
import parsenvy
import unittest

import pytest


def test_boolean_true():
    os.environ["BOOL_TRUE"] = "true"
    assert parsenvy.bool("BOOL_TRUE") is True

    os.environ["BOOL_1"] = "1"
    assert parsenvy.bool("BOOL_1") is True


def test_boolean_false():
    os.environ["BOOL_FALSE"] = "false"
    assert parsenvy.bool("BOOL_FALSE") is False

    os.environ["BOOL_0"] = "0"
    assert parsenvy.bool("BOOL_0") is False


def test_boolean_none():
    assert parsenvy.bool("BOOL_NONE") is None


def test_boolean_default():
    assert parsenvy.bool("BOOL_NONE", "foo") == "foo"


def test_boolean_error():
    os.environ["BOOL_EMPTY"] = ""
    with pytest.raises(ValueError):
        parsenvy.bool("BOOL_EMPTY")

    os.environ["BOOL_STR"] = "nope"
    with pytest.raises(ValueError):
        parsenvy.bool("BOOL_STR")


def test_int_int():
    os.environ["INT_2"] = "2"
    assert parsenvy.int("INT_2") == 2


def test_int_none():
    assert parsenvy.int("INT_NONE") is None


def test_int_default():
    assert parsenvy.int("INT_NONE", 3) == 3


def test_int_error():
    os.environ["INT_EMPTY"] = ""
    with pytest.raises(TypeError):
        parsenvy.int("INT_EMPTY")

    os.environ["INT_STR"] = "nope"
    with pytest.raises(TypeError):
        parsenvy.int("INT_STR")


def test_float_float():
    os.environ["FLOAT_1_23"] = "1.23"
    assert parsenvy.float("FLOAT_1_23") == 1.23


def test_float_none():
    assert parsenvy.float("FLOAT_NONE") is None


def test_float_default():
    assert parsenvy.float("FLOAT_NONE", 1.23) == 1.23


def test_float_error():
    os.environ["FLOAT_EMPTY"] = ""
    with pytest.raises(TypeError):
        parsenvy.float("FLOAT_EMPTY")

    os.environ["FLOAT_STR"] = "nope"
    with pytest.raises(TypeError):
        parsenvy.float("FLOAT_STR")


def test_list_list():
    os.environ["LIST_A_B_C"] = "a,b,c"
    assert parsenvy.list("LIST_A_B_C") == ["a", "b", "c"]


def test_list_none():
    assert parsenvy.list("LIST_NONE") is None


def test_list_empty():
    os.environ["LIST_EMPTY"] = ""
    assert parsenvy.list("LIST_EMPTY") is None


def test_list_default():
    assert parsenvy.list("LIST_NONE", [1, 2]) == [1, 2]


def test_tuple_tuple():
    os.environ["TUPLE_HELLO_WORLD"] = "hello,there,world"
    assert parsenvy.tuple("TUPLE_HELLO_WORLD") == ("hello", "there", "world")


def test_tuple_none():
    assert parsenvy.tuple("TUPLE_NONE") is None


def test_tuple_empty():
    os.environ["TUPLE_EMPTY"] = ""
    assert parsenvy.tuple("TUPLE_EMPTY") is None


def test_tuple_default():
    assert parsenvy.tuple("TUPLE_NONE", ("hello", "there", "world")) == (
        "hello",
        "there",
        "world",
    )


def test_str_list():
    os.environ["STR_HELLO"] = "hello"
    assert parsenvy.str("STR_HELLO") == "hello"


def test_str_empty():
    os.environ["STR_EMPTY"] = ""
    assert parsenvy.str("STR_EMPTY") is None


def test_str_none():
    assert parsenvy.str("STR_NONE") is None


def test_str_default():
    assert parsenvy.str("STR_NONE", "hi") == "hi"


def test_set_set():
    os.environ["SET_A_B_C"] = "a,b,c"
    assert parsenvy.set("SET_A_B_C") == set(["a", "b", "c"])


def test_set_none():
    assert parsenvy.set("SET_NONE") is None


def test_set_empty():
    os.environ["SET_EMPTY"] = ""
    assert parsenvy.set("SET_EMPTY") is None


def test_set_default():
    assert parsenvy.set("SET_NONE", set([1, 2])) == set([1, 2])
