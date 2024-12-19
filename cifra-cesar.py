def cifrar_caractere(caractere, seq, chave):
    indice_atual = seq.index(caractere)
    novo_indice = indice_atual + chave
    while novo_indice >= len(seq):
        novo_indice = novo_indice - len(seq)
    while novo_indice < 0:
        novo_indice = novo_indice + len(seq)
    return seq[novo_indice]

texto = 'aprendendo python'
chave = 4

minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABDCEFGHIJKLMNOPQRSTUVWXYZ'

cifra = ''
for caractere in texto:
    if caractere in minusculas:
        caractere_cifra = cifrar_caractere(caractere, minusculas, chave)
    elif caractere in maiusculas:
        caractere_cifra = cifrar_caractere(caractere, maiusculas, chave)
    else:
        caractere_cifra = caractere
    cifra += caractere_cifra

print(cifra)
