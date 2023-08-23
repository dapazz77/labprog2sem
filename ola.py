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
    saldo = float(input('Saldo R$: '))
    print (f'Saldo com reajuste de 2% = R$ {saldo*1.02}')

def q14():
    numero1 = float(input('Digite a base do retângulo: '))
    numero2 = float(input('Digite a altura do retângulo: '))
    
    result1 = numero1+numero2
    result2 = numero1*numero2

    print (f'O perímetro desse retangulo é: {result1}')
    print (f'O valor da área desse retangulo é: {result2}')

def q15(): 
    valorprod = float(input('Digite o valor do produto: $ '))
    desc = float(input('Digite o percentual do desconto: '))

    valorfim = valorprod*desc/100

    print (f'Desconto: R${valorfim}')
    print (f'Valor final do produto: R${valorprod-valorfim}')

def q16():
    salario = float(input('Qual seu salario atual?: R$'))
    reajuste = float(input('Qual é o valor do reajuste: '))

    valorfim = salario*reajuste/100

    print (f'Seu novo salario é: R${valorfim}')

def q17():
    celsius = float(input('Digite a temperatura em celcius: '))
    fharen = float(input('Digite a temperatura em fahrenheit: '))

    fharen = (9*celsius+160)/5
    result = fharen

    print (f'O valor da conversão é: {result}')

def q18():
    vtempo = float(input('Informe o tempo da viagem em horas: '))
    velmedia = float(input('Informe a velocidade média em KM/H: '))
    
    vdist = vtempo*velmedia
    litros = vdist/12

    print (f'A distancia percorrida foi {vdist} e a quantidade de litros usada foi {litros}L')

def q1l2():
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite um número: '))

    result = n1 + n2

    if result > 10:
        print (f'{result} é maior que 10')

def q2l2():
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite um número: '))
    
    result = n1 + n2

    if result > 20:
        result = result + 8
        print (f'{result}')
    else: 
        result <= 20
        result = result -5
        print (f'{result}')

def q3l2():
    n = float(input('Digite um número: '))

    if n % 3 == 0:
        print('é multiplo de 3')
    else:
        print('não é multiplo 3')

def q4l2():
    n = float(input('Digite um número: '))

    if n % 5 == 0:
        print('é divisivel por 5')
    else:
        print('não é divisivel por 5')

def q4l2():
    n = float(input('Digite um número: '))

    

q4l2()

