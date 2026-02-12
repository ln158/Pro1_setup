from lib.greet import greet

def test_greet_returns_correct_message():
    expected = "Hello, Alice!"

    result = greet("Alice")

    assert result == expected 