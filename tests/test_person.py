from lib.person import Person
from unittest.mock import patch

def xtest_person_instantiates():
    person = Person('Magdalena')

    assert person.name == 'Magdalena'

def xtest_person_go_out_takes_sunglasses_if_sunny():
    person = Person("Magdalena")

    assert person.tries_to_go_out() == "It's sunny outside, let's take sunglasses and go out!"

def xtest_person_go_out_takes_umbrella_if_rainy():
    person = Person("Magdalena")

    assert person.tries_to_go_out() == "It's rainy outside, let's take the umbrella and go out!"





















    # with patch('my_module.random.choice') as weather:
    #     weather.return_value = 'sunny'
    #     result = go_out_function()
    #     assert result == 'my string for sunny'