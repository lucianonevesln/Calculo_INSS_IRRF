def calcula_INSS (salarioBruto):

    if salarioBruto <= 1100.00:
        salarioBrutoINSS = salarioBruto - (salarioBruto * 0.075)
        inss = salarioBruto * 0.075
    elif salarioBruto > 1100.00 and salarioBruto <= 2203.48:
        salarioBrutoINSS = salarioBruto - (salarioBruto * 0.09 - 16.50)
        inss = salarioBruto * 0.09 - 16.50
    elif salarioBruto > 2203.48 and salarioBruto <= 3305.22:
        salarioBrutoINSS = salarioBruto - (salarioBruto * 0.12 - 82.60)
        inss = salarioBruto * 0.12 - 82.60
    elif salarioBruto > 3305.22 and salarioBruto <= 6433.57:
        salarioBrutoINSS = salarioBruto - (salarioBruto * 0.14 - 148.71)
        inss = salarioBruto * 0.14 - 148.71
    elif salarioBruto > 6433.57:
        salarioBrutoINSS = salarioBruto - 751.98
        inss = 751.98
    return salarioBruto, inss, salarioBrutoINSS

def calcula_IRRF(salarioBruto):
    if salarioBruto > 4664.68:
        salarioBrutoIRRF = salarioBruto - (salarioBruto * 0.275 - 869.36)
        irrf = salarioBruto * 0.275 - 869.36
    elif salarioBruto <= 4664.68 and salarioBruto >= 3751.06:
        salarioBrutoIRRF = salarioBruto - (salarioBruto * 0.225 - 636.13)
        irrf = salarioBruto * 0.225 - 636.13
    elif salarioBruto <= 3851.05 and salarioBruto >= 2826.66:
        salarioBrutoIRRF = salarioBruto - (salarioBruto * 0.15 - 354.80)
        irrf = salarioBruto * 0.15 - 354.80
    elif salarioBruto <= 2826.65 and salarioBruto >= 1903.99:
        salarioBrutoIRRF = salarioBruto - (salarioBruto * 0.075 - 142.80)
        irrf = salarioBruto * 0.075 - 142.80
    elif salarioBruto <= 1903.98:
        salarioBrutoIRRF = salarioBruto
        irrf = 0.00
    return salarioBruto, irrf, salarioBrutoIRRF

print("\n--------------------------------------------------\n")

salarioBruto = float(input("Digite o salário bruto: "))

contador1 = 0

print("\n--------------------------------------------------")

for item in calcula_INSS(salarioBruto):
    if contador1 == 1:
        print("\nSalário Bruto: ", salarioBruto)
        inss = calcula_INSS(salarioBruto)
        print("\n(-) INSS: ", round(inss[1], 2))
    contador1 += 1

contador2 = 0

for item in calcula_INSS(salarioBruto):
    if contador2 == 2:
        irrf = calcula_IRRF(item)
        print("(-) IRRF: ", round(irrf[1], 2))
        print("\nSalário Líquido: ", round(irrf[2], 2 ))
    contador2 += 1

print("\n--------------------------------------------------")