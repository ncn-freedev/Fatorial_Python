'''
Este programa consiste em receber um número inteiro do usuário 
e fazer o fatorial deste número
'''

def fatorialFunc(number):
    if number == 1:
       return 1
    else:
        print(number)
        number *= fatorialFunc(number-1)
        return number


finish = True
fatorial = -1

while finish:
    try:
        number = input("Digite o número que desejar realizar o fatorial ou digite sair para finalizar\n")
        number = number.lower()
        if number == 'sair':
            finish = False
        else:
            fatorial = fatorialFunc(int(number))
            print(f'O fatorial do número {number} é {fatorial}\n')
    except:
            print("Você deve digitar um número para que seja feito o fatorial ou a palavra \"Sair\" para poder sair\n")

print('Fim do programa')
     