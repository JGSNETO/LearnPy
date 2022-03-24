"""
Introdução ao módulo Unittest

Unittest->Testes unitários.

O que são testes unitários ?

Teste unitário é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: Funções, Métodos, Classes, módulos, etc..

OBS: Teste unitário não é específico da linguagem python. 

Para criar nossos testes criamos calsses que herdam do unittest. TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de teste para sua unidade

docs.python.org/3/library/unittest
#Conhecendo as assertions
Método                Checa que
assertEqueal(a,b)       a==b
assertNotEqual(a,b)     a!=b
assertTrue(X)           x é verdadeiro
.
.
.
.

Por convenção todos os testes em um teste case devem ter seus nomes iniciados com "test_"

#Para executar os testes no módo verboso: python programa.py -v
"""
#Prática utilizando a abordagem TDD


