"""Kleine Taschenrechner-Bibliothek."""


def summe(zahlen):
    return sum(zahlen)


def durchschnitt(zahlen):
    if not zahlen:
        raise ValueError("Liste ist leer")
    return summe(zahlen) / len(zahlen)


def prozent(teil, ganzes):
    if ganzes == 0:
        raise ValueError("Ganzes darf nicht 0 sein")
    return teil / ganzes * 100
