from _pytest.capture import CaptureFixture

from src.decorators import log, my_function


def test_log_1(capsys: CaptureFixture):
    log()(my_function)(1, 2)
    captured = capsys.readouterr()
    assert captured.out == 'my_function, "ok"\n'
    log()(my_function)("1", 2)
    captured = capsys.readouterr()
    assert captured.out == (
        'my_function, "TypeError" can only concatenate str (not "int") to str, ' "Inputs: ('1', 2), {}\n"
    )


def test_log_2():
    log(filename="mylog.txt")(my_function)(1, 2)
    with open("mylog.txt", "r") as file:
        a = file.readlines()
        assert a[-1] == 'my_function, "ok"\n'
    log(filename="mylog.txt")(my_function)("1", 2)
    with open("mylog.txt", "r") as file:
        a = file.readlines()
        assert a[-1] == (
            'my_function,"TypeError" can only concatenate str (not "int") to str, ' "Inputs: ('1', 2), {}\n"
        )
