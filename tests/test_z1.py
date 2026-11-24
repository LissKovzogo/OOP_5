import sys
import os
# tests/test_z1.py
import pytest
from oop_5.Zadania.z_1 import pair, run_check


def test_pair_valid():
    assert pair(("Возраст", 25)) == "Возраст — 25"

def test_run_check_success(capsys):
    result = run_check(("Возраст", 25))

    captured = capsys.readouterr()
    assert result == "Возраст — 25"
    assert "Первый элемент — строка: True" in captured.out
    assert "Второй элемент — целое число: True" in captured.out
    assert "Результат: Возраст — 25" in captured.out

def test_run_check_invalid_first_type(capsys):
    result = run_check((25, 25))

    captured = capsys.readouterr()
    assert result == "Ошибка"
    assert "Первый элемент — строка: False" in captured.out
    assert "Ошибка: типы данных не соответствуют аннотации." in captured.out

def test_run_check_invalid_second_type(capsys):
    result = run_check(("Возраст", "25"))

    captured = capsys.readouterr()
    assert result == "Ошибка"
    assert "Второй элемент — целое число: False" in captured.out
    assert "Ошибка: типы данных не соответствуют аннотации." in captured.out