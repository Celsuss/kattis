import pytest
import main


def test_main_1(monkeypath):
    inputs = iter(['1 4', '1100', '2', '1114', '1111'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))

    res = main.main()
    answer = ['neither', 'decimal']
    assert(len(res) == len(answer))
    for a in answer:
        assert(a in res)


def test_main_2(monkeypath):
    inputs = iter(['10', '20',
                   '11111111111111111111',
                   '11000000000000000101',
                   '11111111111111110000',
                   '11111111111111110000',
                   '11000000000000000111',
                   '00011111111111111111',
                   '00111111111111111111',
                   '10000000000000001111',
                   '11111111111111111111',
                   '11111111111111111111',
                   '3',
                   '2 3 8 16',
                   '8 1 7 3',
                   '1 1 10 20',
                   ])
    monkeypatch.setattr('builtins.input', lambda: next(inputs))

    res = main.main()
    answer = ['neither', 'decimal']
    assert(len(res) == len(answer))
    for a in answer:
        assert(a in res)
