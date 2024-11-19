import meu_modulo
#aprendendo python conceitos basicos 5a parte - primeira aula

def somar_dois(n):
    return n + 2
resultado = somar_dois(10)    
print(resultado)

def concatenar_texto(t1, t2):
    return t1+t2
print(concatenar_texto('bbebebebe ', 'abababa'))

def adicionar_final(texto, final="!!!"):
    return texto + final
print(adicionar_final('Olá'))

def dividir(a,b):
    if b == 0:
        return 'Impossivel dividir!'
    return a/b
print(dividir(10, 5))

#usando a importacao do modulo

retorno = meu_modulo.minha_funcao()

print(retorno)
print(meu_modulo.x)