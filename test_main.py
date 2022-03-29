import pytest
import primepalin


#@pytest.mark.skip(reason = "something")
@pytest.mark.parametrize("a,b",[(3,"prime"),(4,"not prime"),(5,"prime")])
def test_prime(a,b):
    r1 = primepalin.prime(a)
    assert r1 ==b


#@pytest.mark.xfail
@pytest.mark.parametrize("a,b",[(343,"palindrome"),(1221,"palindrome"),(5005,"palindrome")])
def test_palin(a,b):
    r2 = primepalin.palin(a)
    assert r2 == b