def add(a, b):
    add_result = a + b
    print("Resultado da soma: " + str(add_result))

def subtraction(a,b):
    subtraction_result = a - b
    print("Resultado da subtração: " + str(subtraction_result))

def multiplication (a,b):
    multiplication_result = a * b
    print("Resultado da Multiplicação: " + str(multiplication_result))

def division (a,b):
    if(a == 0 or b == 0):
        print("Não é possível dividir por zero")
    else :
        division_result = a / b
        print("Resultado da divisão: " + str(division_result))

def power (valueToCalc, powerNumber):
    if(powerNumber == 1):
        print("Resultado da potenciação: " + str(valueToCalc))
    elif (powerNumber == 0):
        print("Resultado da potenciação: 1")
    else:
        resultado_potenciacao = valueToCalc ** powerNumber
        print("Resultado da potenciação: " + str(resultado_potenciacao))

def module(a,b):
    module_result = a % b
    print("Resultado do módulo: " + str(module_result))

def raiz(a):
    result = a ** (1/2)
    print("Resultado da raiz: " + str(result))

def plusOne(a):
    result = a + 1
    print("Resultado Plus One: " + str(result))

def celsiusToFahrenheit(celsiusValue):
    farenheitValue = (celsiusValue * 1.8) + 32
    print("Valor em Fahrenheit: " + str(farenheitValue))


add(1, 1)
subtraction(1, 10)
multiplication(2,3)
division(0,1)
division(10,2)
power(2,0)
module(10,2)
raiz(8)
plusOne(10)
celsiusToFahrenheit(int(input("Digite a temperatura de atual...")))


