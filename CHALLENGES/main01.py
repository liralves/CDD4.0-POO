from classes import *
P1 = Person("", 20, 80)
OP = 0
P1.name = input("Digite o nome da pessoa: ")
while OP != 7:
    OP = int(input(f"O que {P1.name} irá fazer? \n1.COMER | 2.FALAR | 3.DORMIR | 4.PARAR DE COMER | 5.PARAR DE FALAR | 6.PARAR DE DORMIR | 7.SAIR\n"))
    while OP < 1 or OP > 7:
        print("Valor inválido. Digite as opções de acordo com o MENU:")
        OP = int(input(f"O que {P1.name} irá fazer? \n1.COMER | 2.FALAR | 3.DORMIR | 4.PARAR DE COMER | 5.PARAR DE FALAR | 6.PARAR DE DORMIR | 7.SAIR\n"))
    if OP == 1:
        P1.eat()
    elif OP == 2:
        P1.talk()
    elif OP == 3:
        P1.sleep()
    elif OP == 4:
        P1.stopEat()
    elif OP == 5:
        P1.stopTalk()
    else:
        P1.stopSleep()
