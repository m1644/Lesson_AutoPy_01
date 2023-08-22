from main import check_words


def test_step1(good, bad):
    assert good in check_words(bad)
