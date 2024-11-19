import math

print(math.pi)
print(math.log(16, 2))

import datetime
agora = datetime.datetime.now()
ano_2000 = datetime.datetime(2000, 1, 1)

print(datetime.datetime.now())
print(agora - ano_2000)


import random
for _ in range(2):
    n = random.randint(1, 10)
    print(n)
nomes = ['Juliano', 'Marcos', 'Paulo']

for _ in range (2):
    nome = random.choice(nomes)
    print(nome)