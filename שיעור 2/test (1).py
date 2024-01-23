import pytest
import main




@pytest.mark.parametrize("num1,list", [( 4, {1, 2, 3}), (1, {1, 2, 3, 5, 7}), ('a', 4, {1, 3})])
def test_find_prime(num1,list):
    assert main.find_prime(num1)==list


@pytest.mark.parametrize("listBefore,listAfter", [ ({1,4,3,6 }, {1, 3, 4,6}), ('a',  {1, 3})])
def test_sort_list(listBefore,listAfter):
    assert main.sort_list(listBefore)==listAfter

@pytest.mark.tamarayelet
def test_find_primes():
    assert functions.find_prime(5) == {1, 2, 3}
    assert functions.find_prime(7) == {1, 2, 3}
    assert functions.find_prime(-12) == set()

