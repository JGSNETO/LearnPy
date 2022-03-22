"""
Doctests: Testes que colocamos na docstring das funções/métodos python
#Executando no terminal o doctest: python -m doctest -v doctest.py

TDD: Test driven developement def soma (a, b):
    Soma os números a e b

    "Colocar >>>"soma(1,2)
    3
    return a + b
print(soma(3, 4))

OBS: Dentro do docstring o python não reconhece string com aspas duplas, precisa ser aspas simples.
"""
def duplicar(valores):
    """
    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar(['a', 'b' , 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([])
    []
    
    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """

    return [2 * elemento for elemento in valores]