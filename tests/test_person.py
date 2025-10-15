from lib.person import Person
from unittest.mock import patch

def test_person_instantiates():
    person = Person('Magdalena')

    assert person.name == 'Magdalena'

def test_person_go_out_takes_sunglasses_if_sunny():
    person = Person("Magdalena")

    with patch('random.choice') as weather:
        weather.return_value = 'sunny'
        result = person.tries_to_go_out()

    assert result == "It's sunny outside, let's take sunglasses and go out!"

def test_person_go_out_takes_umbrella_if_rainy():
    person = Person("Magdalena")
    with patch('random.choice') as weather:
        weather.return_value = 'rainy'
        result = person.tries_to_go_out()

    assert result == "It's rainy outside, let's take the umbrella and go out!"

# 0-30% : you need revision
# (-1 => error) 0,1, 15, 29,30

# 31-70% : great, you passed
# 31,32, 69,70

# 71-100% : amazing, distinction
# 71, 72, 99,100, 101(error)
