from greetings import greet, farewell


def test_greet_returns_friendly_message():
    assert greet("Sam") == "Hello, Sam!"


def test_farewell_returns_friendly_message():
    assert farewell("Sam") == "Goodbye, Sam. See you soon!"
