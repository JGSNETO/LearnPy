"""
Assertions: Checagens/Questionamentos

Em python utilizamos a palavra reservada  'assert' para realizar simples afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, retorna none e caso seja falsa levanta um erro to tipo
AssertionError.

OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada

OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso .. Não precisa
ser exclusivamente nos testes.
"""

def soma (a,b):

    assert a>0 and b>0, 'Ambos os numeros precisam ser positivos'
    return a + b

ret = soma(2 , 4)

print(ret)

#Alerta cuidado ao usar o 'assert'. Se o programa for executado com o parâmetro -O, nenhum assertion será validado.
