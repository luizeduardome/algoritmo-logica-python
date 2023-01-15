# Listagem 4.3 - Carro velho ou novo, depende da idade.

idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
if idade > 3:
    print("Seu carro é velho")

# Listagem 4.4 - Cálculo do Imposto de Renda
salario = float(input("Digite o salário para cálculo do imposto: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print("Salário: R$%6.2f Imposto a pagar: R$6.2f" % (salario, imposto))
