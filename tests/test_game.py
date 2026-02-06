from game import check_guess

def test_check_guess_true():
    assert check_guess(5, 5) is True

def test_check_guess_false():
    assert check_guess(5, 3) is False
