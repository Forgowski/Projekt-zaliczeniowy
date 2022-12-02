from engine import Engine
from dictionary import Dictionary
from validator import Validator
from stats import Stats
import pytest

dic = Dictionary()
validator = Validator()
stats =Stats()


#sprawdzamy poprawne wybieranie słów do gry
def test_dictionary_random():
    assert dic.random() != ""

#sprawdzamy działanie validatora izogramów
@pytest.mark.parametrize("input, output", [("osa", 1), ("okoń", 0), ("torba", 1), ('barok', 1), ("ala", 0)])
def test_validator(input, output):
    x = len(input)
    assert validator.validWord(input, x) == output

#sprawdzamy działanie zliczania cows
@pytest.mark.parametrize("input, output", [(1, 1), (3, 3), (21, 21), (5, 5), (100, 100)])
def test_stats_addCows(input, output):
    stats.clearCows()
    for i in range(input):
        stats.addCows()
    assert stats.cows == output


#sprawdzamy działanie zliczania bulls
@pytest.mark.parametrize("input, output", [(1, 1), (3, 3), (21, 21), (5, 5), (100, 100)])
def test_stats_addBulls(input, output):
    stats.clearBulls()
    for i in range(input):
        stats.addBulls()
    assert stats.bulls == output