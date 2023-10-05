import pytest
import pinball


def test_pinball_1(monkeypatch):
    inputs = iter(['2', '-1 1 1 -1', '1 -2 2 -3', '0'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))

    res = pinball.main()
    assert(res == 2)


def test_pinball_2(monkeypatch):
    inputs = iter(['3', '-1 1 1 -1', '1 -2 0 -3', '1 -3 2 -4', '0'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    res = pinball.main()
    assert(res == 0)


def test_pinball_3(monkeypatch):
    inputs = iter(['0', '0'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    res = pinball.main()
    assert(res == 0)

def test_pinball_3(monkeypatch):
    inputs = iter(['0', '2'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))
    res = pinball.main()
    assert(res == 2)
