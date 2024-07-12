# questão 1
numero = int(input('Informe um número: '))

intervalo1 = [0, 25]
intervalo2 = [26, 50]
intervalo3 = [51, 75]
intervalo4 = [76, 100]

if intervalo1[0] <= numero <= intervalo1[1]:
    print(f'O número {numero} está no intervalo {intervalo1}')
elif intervalo2[0] <= numero <= intervalo2[1]:
    print(f'O número {numero} está no intervalo {intervalo2}')
elif intervalo3[0] <= numero <= intervalo3[1]:
    print(f'O número {numero} está no intervalo {intervalo3}')
elif intervalo4[0] <= numero <= intervalo4[1]:
    print(f'O número {numero} está no intervalo {intervalo4}')
else:
    print(f'O número {numero} não está em nenhum dos intervalos')
