#questão 3
tipoCombustivel = ['1 - Álcool', '2 - Gasolina', '3 - Diesel', '4 - Fim']
for x in tipoCombustivel:
    print(x)

tipo_combustivel = str(input('Informe o tipo de combustível: '))

if tipo_combustivel == '1':
    print(f'Você escolheu: Álcool. Combustível cadastrado!')
elif tipo_combustivel == '2':
    print(f'Você escolheu: Gasolina. Combustível cadastrado!')
elif tipo_combustivel == '3':
    print(f'Você escolheu: Diesel. Combustível cadastrado!')
elif tipo_combustivel == '4':
    print('Você escolheu sair.')
else:
    print('Código inválido!')
