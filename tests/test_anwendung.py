import pytest

from src.anwendung import durchschnitt, prozent, summe


def test_summe():
    assert summe([1, 2, 3]) == 6


def test_durchschnitt():
    assert durchschnitt([2, 4, 6]) == 4


def test_durchschnitt_leere_liste():
    with pytest.raises(ValueError):
        durchschnitt([])


def test_prozent():
    assert prozent(25, 200) == 12.5
