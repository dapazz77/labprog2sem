def q01():
    print('Higor da Paz Moreno Silva')

def q02():
    print(30,27)

def q03():
    n1 = 5
    n2 = 8 
    n3 = 12

    media = (n1 + n2 + n3)/3

    print (f'A média aritmética entre 5,8 e 12 é: {media}')

def q04():
    numero = (input('Digite um número?: '))

    print (numero)

def q05():
    numero1 = float(input('Digite algum número: '))
    numero2  = float(input('Digite outro número: '))

    print (numero1)
    print (numero2)

def q06():
    numero = int(input('Digite um número: '))

    antecessor = numero-1
    sucessor = numero+1    

    print (f'O antecessor é:  {antecessor}')
    print (f'O sucessor é:  {sucessor}') 

def q07():
    nome = (input('Digite seu nome:'))
    ende = (input('Digite seu endereço: '))
    telefone = (input('Digite seu telefone: '))

    print (nome)
    print (ende)
    print (telefone)

def q08():
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))

    result  = numero1-numero2

    print (f'A subtração é: {result}')

def q09():
    numero = float(input('Digite um número real: '))

    result = numero/4

    print (f'O 1/4 desse númmero é: {result}')

def q10():
    numero1 = float(input('Digite um número real: '))
    numero2 = float(input('Digite um número real: '))
    numero3 = float(input('Digite um número real: '))

    valorfim = numero1+numero2+numero3
    result = valorfim/3

    print (f'A média aritmética desses números é: {result}')

def q11():
    numero1 = float(input('Digite um número real: '))
    numero2 = float(input('Digite outro número real: '))

    result1 = numero1+numero2 
    result2 = numero1-numero2
    result3 = numero1*numero2
    result4 = numero1/numero2

    print (f'A adição desses número é: {result1}')
    print (f'A subtração desses números é: {result2}')
    print (f'A multiplicação desses números é: {result3}')
    print (f'A divisão desses números é: {result4}')

def q12():
    numero = float(input('Digite um número: '))

    result = numero*numero

    print (f'O quadrado desse número é: {result}')

def q13():
    numero = float(input('Digite o seu saldo na poupança: '))

    result = numero- 2/100

    print (f'Seu saldo com o reajuste é: {result}')

def q14():
    numero1 = float(input('Digite a base do retângulo: '))
    numero2 = float(input('Digite a altura do retângulo: '))
    
    result1 = numero1+numero2
    result2 = numero1*numero2


q13()
