import pytest
from tp5 import *

# Test para la función search_last_name 1
@pytest.mark.parametrize("name, resp",[
    (["Ruth", "Condorí"], "Condorí")
])
def test_search_last_name(name, resp):
    assert search_last_name(name) == resp

# Test para la función get_dni_id 2
@pytest.mark.parametrize("dni, resp",[
    (94219667, 942),
    (9421966, 942)
])
def test_get_dni_id(dni, resp):
    assert get_dni_id(dni) == resp

# Test para la función create_id 3
@pytest.mark.parametrize("name, last_name, num_id, resp",[
    (["Paula", "Geier"], "Geier", 445, "Paula5445")
])
def test_create_id(name, last_name, num_id, resp):
    assert create_id(name, last_name, num_id) == resp

# Test para la función Multiples 4
def test_multiples1():
    assert Multiples(10, 2) == True

def test_multiples2():
    assert Multiples(7, 2) == False

# Test para la función space_between_letters 5
def space_word_test1():
    assert space_between_letters('Hola, tu') == 'H o l a, t u'

def space_word_test2():
    assert space_between_letters('Hola, jaja') == 'H o l a, j a j a'

# Test para la función purchase_total 6
@pytest.mark.parametrize('a,res',[
    ({1000:0.10,2000:0.20,3000:0.30,1500:0.10,2500:0.20,3500:0.30},10400),
    ({1500:0.15,2500:0.25,3500:0.35,1550:0.15,2550:0.25,3550:0.35},10962.5)
])
def test_purchase_total(a,res):
    assert purchase_total(a)==res


# Test para la función phrase_to_dict
def test_phrase_to_dict_simple():
    phrase = "Hello World"
    result = phrase_to_dict(phrase)
    expected = {"Hello": 5, "World": 5}
    assert result == expected

def test_phrase_to_dict_varied_lengths():
    phrase = "The quick brown fox jumps over the lazy dog"
    result = phrase_to_dict(phrase)
    expected = {"The": 3, "quick": 5, "brown": 5, "fox": 3, "jumps": 5, "over": 4, "the": 3, "lazy": 4, "dog": 3}
    assert result == expected

# Test para la función calcular_modulo
def test_calcular_modulo():
    vector = [3, 4]
    modulo = calc_modulo_vector(vector)
    assert modulo == 5.0

# Test para la función es_primo
def test_es_primo():
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(4) == False
    assert is_prime(1) == False

# Test para la función calcular_factorial
def test_calcular_factorial():
    assert calc_factorial(5) == 120
    assert calc_factorial(0) == 1
