import pytest

from .string_functions import *

def test_greeting_jeremy():
    """Test for greet_by_name"""
    # Step 1: Choose a scenario - here I'm choosing name='Jeremy'

    # Step 2: Decide what the expected outcome is for the scenario
    expected = 'Hello, Jeremy!'

    # Step 3: Call the function being tested to get its actual output
    actual = greet_by_name('Jeremy')

    # Step 4: Compare expected & actual outcomes. If they match, the test passes
    assert actual == expected

def test_greeting_dani():
    """Test for greet_by_name"""
    expected = 'Hello, Dani!'
    actual = greet_by_name('Dani')
    assert actual == expected

def test_reverse_long():
    """Test reversing a long string."""
    expected = 'qwertyuiop'
    actual = reverse('poiuytrewq')
    assert actual == expected

def test_reverse_short():
    """Test reversing a short string."""
    expected = 'asdf'
    actual = reverse('fdsa')
    assert actual == expected

def test_reverse_words_long():
    """Test reversing words in a long string."""
    expected = 'olleH ym eman si ,nagoL tahw si ?sruoy'
    actual = reverse_words('Hello my name is Logan, what is yours?')
    assert actual == expected

def test_reverse_words_short():
    """Test reversing words in a short string."""
    expected = ',woW !emosewa'
    actual = reverse_words('Wow, awesome!')
    assert actual == expected

def test_sarcastic_long():
    """Test sarcastic-ifying a long string."""
    expected = 'ThIs Is ThE sArCaStIc StRiNg TeSt.'
    actual = sarcastic('This is the sarcastic string test.')
    assert actual == expected

def test_sarcastic_short():
    """Test sarcastic-ifying a short string."""
    expected = 'Oh YeAh.'
    actual = sarcastic('Oh yeah.')
    assert actual == expected

def test_find_longest_word():
    with pytest.raises(Exception):
        expected = 'yeah'
        actual = sarcastic('Oh yeah')
        assert actual == expected

# run the tests
if __name__ == '__main__':
    unittest.main()