# obter o valor total

renda_mendal = float(input("Digite sua Renda mensal: "))

# obtendo aa porcentagem

obtendo_50_porcento = (50 / 100) * renda_mendal
obtendo_30_porcento = (30 / 100) * renda_mendal
obtendo_20_porcento = (20 / 100) * renda_mendal

print("=================\nSeus Numeros de 50% 30% 20%\n=================")

print("Necessidades: R${:,.2f}".format(obtendo_50_porcento))
print("Pretende Gastar: R${:,.2f}".format(obtendo_30_porcento))
print("Economias: R${:,.2f}".format(obtendo_20_porcento))

print("==================================")