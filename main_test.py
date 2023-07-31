import main


def larger_test(capsys, monkeypatch):
    inputs = iter([3571, 56872])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.larger()
    captured = capsys.readouterr()
    assert captured.out == '56872\n'


def boolean_test(capsys):
    main.boolean()
    captured = capsys.readouterr()
    assert captured.out == 'Wahr\n'


def modulo_test1(capsys, monkeypatch):
    inputs = iter([17])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.modulo()
    captured = capsys.readouterr()
    assert captured.out == 'odd\n'


def modulo_test2(capsys, monkeypatch):
    inputs = iter([68])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.modulo()
    captured = capsys.readouterr()
    assert captured.out == 'even\n'


def nested_test1(capsys, monkeypatch):
    inputs = iter([-5])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.nested()
    captured = capsys.readouterr()
    assert captured.out == 'Less than zero\n'


def nested_test2(capsys, monkeypatch):
    inputs = iter([197])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.nested()
    captured = capsys.readouterr()
    assert captured.out == 'Greater than 100\n'


def nested_test3(capsys, monkeypatch):
    inputs = iter([63])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.nested()
    captured = capsys.readouterr()
    assert captured.out == 'Between 0 and 100\n'
