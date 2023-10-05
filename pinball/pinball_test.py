import pytest
import pinball


def test_pinball_1(monkeypatch):
    inputs = iter(['2', '-1 1 1 -1', '1 -2 2 -3' '0'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))

    res = pinball.main()
    assert(res == 2)

    return 0
