def fizzbuzz(n):
    return "Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0) or str(n)


def check_fizzbuzz(value, expected_result):
    actual = fizzbuzz(value)
    assert actual == expected_result


def test_returns_1_with_1_passed_in():
    check_fizzbuzz(1, "1")


def test_returns_2_with_2_passed_in():
    check_fizzbuzz(2, "2")


def test_returns_fizz_with_3_passed_in():
    check_fizzbuzz(3, "Fizz")


def test_returns_buzz_with_5_passed_in():
    check_fizzbuzz(5, "Buzz")


def test_returns_fizz_with_6_passed_in():
    check_fizzbuzz(6, "Fizz")


def test_returns_buzz_with_10_passed_in():
    check_fizzbuzz(10, "Buzz")


def test_returns_fizzbuzz_with_15_passed_in():
    check_fizzbuzz(15, "FizzBuzz")
