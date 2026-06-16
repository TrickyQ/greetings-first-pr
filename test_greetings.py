from greetings import greet


def test_greet_returns_friendly_message():
    assert greet("Sam") == "Hello, Sam!"
