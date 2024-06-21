from random import randint

def sorteia(lis):
    for c in range(0, 6):
       lis.append(randint(0, 10))
    print(f'numeros sorteadops: {lis}')

def somapar(lis):
    soma =0
    for c in lis:
        if c %2 == 0:
            soma += c
    print(f'a soma dos numeros pares é de {soma}')


num = []
sorteia(num)
somapar(num)
print('fim')