import random

n = -1

while n < 5:
    n = int(input('Taper la plus grand valeur a esstime : '))
    if n < 5:
        print('doit etre superieur strictement a 5')
n = random.randint(1, n)
gess = int(input('le nombre que vous estimez est :'))
i = 1
while gess != n:
    if gess > n:
        gess = int(
            input('le  but est plus petit que {} , Ressayer : '.format(gess)))
    if gess < n:
        gess = int(
            input('le  but est plus grand que {} , Ressayer : '.format(gess)))
    i = i + 1
print(
    ' Filecitation, {0} est le nombre correct. le nombre d\'essaye est {1} '.format(n, i))
