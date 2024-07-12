#questão 4:
tipoCombustivel = ['1 - Álcool - R$ 4,00', '2 - Gasolina - R$ 5,95', '3 - Diesel - R$ 6,50', '4 - Fim']
for x in tipoCombustivel:
    print(x)

precoLitro_Alcool = 4.00
precoLitro_Gasolina = 5.95
precoLitro_Diesel = 6.50

tipo_combustivel = str(input('Informe o tipo de combustível: '))
valorPagamento = float(input('Informe o valor do pagamento: '))

if tipo_combustivel == '1':
    totalLitros = valorPagamento / precoLitro_Alcool
    print(f'Você escolheu: Álcool. Combustível cadastrado! E total L: {round(totalLitros, 2)} L')
elif tipo_combustivel == '2':
    totalLitros = valorPagamento / precoLitro_Gasolina
    print(f'Você escolheu: Gasolina. Combustível cadastrado! E total L: {round(totalLitros, 2)} L')
elif tipo_combustivel == '3':
    totalLitros = valorPagamento / precoLitro_Diesel
    print(f'Você escolheu: Diesel. Combustível cadastrado! E total L: {round(totalLitros, 2)} L')
elif tipo_combustivel == '4':
    print('Você escolheu sair.')
else:
    print('Código inválido!')
