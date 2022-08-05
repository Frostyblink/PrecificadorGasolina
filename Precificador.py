#ENTRADA
largura = float(input('Largura do tanque (Em centímetros):'))
altura = float(input('altura do tanque (Em centímetros):'))
profundidade = float(input('profundidade ( Em centímetros):'))
palcool = 1.50
pgasolina = 2.00

#PROCESSAMENTO
v = largura * altura * profundidade
alcoolpl = v * palcool
gasolinapl = v * pgasolina

#SAIDA
print(f'Se você abastecer somente com gasolina, você irá pagar {gasolinapl} enchendo 100% do tanque, mas se encher somente com álcool, você irá pagar {alcoolpl}')
