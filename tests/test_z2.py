import sys
import os

# tests/test_z2.py
import pytest
from oop_5.Zadania.z_2 import filter_collection

def is_even(x):
    return x % 2 == 0

def test_filter_list():
    input_list = [1, 2, 3, 4, 5, 6]
    result = filter_collection(input_list, is_even)

    assert isinstance(result, list)
    assert result == [2, 4, 6]

def test_filter_tuple():
    input_tuple = (10, 15, 20, 25)
    result = filter_collection(input_tuple, is_even)

    assert isinstance(result, tuple)
    assert result == (10, 20)

def test_filter_set():
    input_set = {1, 2, 3, 4, 5}
    result = filter_collection(input_set, is_even)

    assert isinstance(result, set)
    assert result == {2, 4}

def test_filter_empty_result():
    input_list = [1, 3, 5]
    result = filter_collection(input_list, is_even)

    assert result == []
    assert isinstance(result, list)

def test_filter_with_strings():
    def is_long_word(word):
        return len(word) > 3

    input_list = ["cat", "dog", "elephant", "fox"]
    result = filter_collection(input_list, is_long_word)

    assert result == ["elephant"]

