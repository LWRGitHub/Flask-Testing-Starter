import pytest

from .app import app

#######################
# Index Tests
# (there's only one here because there is only one possible scenario!)
#######################

def test_index():
    """Test that the index page shows "Hello, World!" """
    res = app.test_client().get('/')
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = "Hello, World!"
    assert expected_page_text == result_page_text


#######################
# Color Tests
#######################

def test_color_results_blue():
    """ tests of the input blue """
    result = app.test_client().get('/color_results?color=blue')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'Wow, blue is my favorite color, too!'
    assert expected_page_text == result_page_text

def test_color_results_light_green():
    """ test of the input light green """
    result = app.test_client().get('/color_results?color=light%20green')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'Wow, light green is my favorite color, too!'
    assert expected_page_text == result_page_text

def test_color_results_empty():
    """ checks if it can handle an empty input """
    result = app.test_client().get('/color_results?color=')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You didn't specify a color!"
    assert expected_page_text == result_page_text


#######################
# Froyo Tests
#######################

def test_froyo_results_str():
    """ string words tested """
    result = app.test_client().get('/froyo_results?flavor=froot&toppings=sprinkl')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You ordered froot flavored Fro-Yo with toppings sprinkl!"
    assert expected_page_text == result_page_text

def test_froyo_results_numbers():
    """ numbers enterd tested """
    result = app.test_client().get('/froyo_results?flavor=123456&toppings=09876543')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You ordered 123456 flavored Fro-Yo with toppings 09876543!'
    assert expected_page_text == result_page_text

def test_froyo_results_spaces():
    """ checks if spaces work """
    result = app.test_client().get('/froyo_results?flavor=whipped&toppings=sprinkls%20chocolet%20Chips')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = 'You ordered whipped flavored Fro-Yo with toppings sprinkls chocolet Chips!'
    assert expected_page_text == result_page_text

def test_froyo_results_empty():
    """ tests and empty input """
    result = app.test_client().get('/froyo_results?flavor=&toppings=')

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You didn't specify a flavor & or toppings!"
    assert expected_page_text == result_page_text


#######################
# Reverse Message Tests
#######################

def test_message_results_helloworld():
    form_data = {
        'message': 'Hello World'
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'dlroW olleH' in result_page_text

def test_message_results_long_sentence():
    """ testing a long sentence """
    form_data = {
        'message': "Wow, I just don't know how in the world this has happened!"
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "!deneppah sah siht dlrow eht ni woh wonk t'nod tsuj I ,woW" in result_page_text

def test_message_results_empty():
    """ testing an empty string """
    form_data = {
        'message': ""
    }
    res = app.test_client().post('/message_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert 'You set us nothing WHAT "lol" are you doing! You muct type something "lol!"' in result_page_text


#######################
# Calculator Tests
#######################

def test_calculator_results_num_plus():
    """ tests the add operation """
    form_data = {
        'operand1': '2',
        'operand2': '4',
        'operation': 'add'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert f'You chose to add 2 and 4. Your result is: 6' in result_page_text

def test_calculator_results_srt_num():
    """ test to see if the func can do string numbers """
    form_data = {
        'operand1': '2',
        'operand2': '4',
        'operation': 'add'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert f'You chose to add 2 and 4. Your result is: 6' in result_page_text

def test_calculator_results_neg_num():
    """ tests to see if the func can do negative numbers """ 
    form_data = {
        'operand1': '-2',
        'operand2': '-4',
        'operation': 'subtract'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert f'You chose to subtract -2 and -4. Your result is: 2' in result_page_text

def test_calculator_results_multiply():
    """ tests multiply  """
    form_data = {
        'operand1': '2',
        'operand2': '4',
        'operation': 'multiply'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert f'You chose to multiply 2 and 4. Your result is: 8' in result_page_text

def test_calculator_results_num():
    """ tests if the function can handle an int """ 
    form_data = {
        'operand1': 2,
        'operand2': 4,
        'operation': 'add'
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert f'You chose to add 2 and 4. Your result is: 6' in result_page_text

def test_calculator_results_empty():
    """ test to see if the function can deal with an empty string """
    form_data = {
        'operand1': '',
        'operand2': '',
        'operation': ''
    }
    res = app.test_client().post('/calculator_results', data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "Please enter two numbers and an operation." in result_page_text