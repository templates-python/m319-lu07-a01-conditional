import main


def test_larger(capsys, monkeypatch):
    inputs = iter([3571, 56872])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.larger()
    captured = capsys.readouterr()
    assert captured.out == '56872 is greater\n'


def test_boolean(capsys):
    main.boolean()
    captured = capsys.readouterr()
    assert captured.out == 'Wahr\n'


def test_modulo1(capsys, monkeypatch):
    inputs = iter([17])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.modulo()
    captured = capsys.readouterr()
    assert captured.out == 'You entered 17 which is an odd integer.\n'


def test_modulo2(capsys, monkeypatch):
    inputs = iter([68])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.modulo()
    captured = capsys.readouterr()
    assert captured.out == 'You entered 68 which is an even integer.\n'


def test_nested1(capsys, monkeypatch):
    inputs = iter([-5])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.nested()
    captured = capsys.readouterr()
    assert captured.out == 'Less than zero\n'


def test_nested2(capsys, monkeypatch):
    inputs = iter([197])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.nested()
    captured = capsys.readouterr()
    assert captured.out == 'Greater than 100\n'


def test_nested3(capsys, monkeypatch):
    inputs = iter([63])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.nested()
    captured = capsys.readouterr()
    assert captured.out == 'Between 0 and 100\n'
