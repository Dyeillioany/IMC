peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"seu IMC é {imc:.2f} e voce está: Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print(f"seu IMC é {imc:.2f} e voce está com: Peso normal")
elif imc >= 25 and imc <= 29.9:
    print(f"seu IMC é {imc:.2f} e voce está: Sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print(f"seu IMC é {imc:.2f} e voce está com : Obesidade grau I")
elif imc >= 35 and imc <= 39.9:
    print(f"seu IMC é {imc:.2f} e voce está com: Obesidade grau II")
else:
    print(f"seu IMC é {imc:.2f} e voce está com: Obesidade grau III")