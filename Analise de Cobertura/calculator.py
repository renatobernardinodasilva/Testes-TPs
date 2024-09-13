import math

def calculator():
    while True:
        print("\nSelecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potência")
        print("6. Raiz quadrada")
        print("7. Sair")

        escolha = input("Digite a escolha (1/2/3/4/5/6/7): ")

        if escolha == '7':
            print("Saindo da calculadora.")
            break

        if escolha in ['1', '2', '3', '4', '5']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif escolha == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
            elif escolha == '5':
                print(f"{num1} elevado a {num2} = {num1 ** num2}")

        elif escolha == '6':
            num = float(input("Digite o número para a raiz quadrada: "))
            print(f"Raiz quadrada de {num} = {math.sqrt(num)}")

        else:
            print("Escolha inválida, por favor tente novamente.")
