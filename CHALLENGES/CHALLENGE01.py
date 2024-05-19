class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.talking = False
        self.eating = False
        self.sleeping = False

    def eat(self):
        if self.talking == True:
            print(f"{self.name} não pode comer, pois está falando.")
        elif self.sleeping == True:
            print(f"{self.name} não pode comer, pois está dormindo.")
        elif self.eating==True:
            print(f"{self.name} já estava comendo.")
        else:
            self.eating = True
            print(f"{self.name} está comendo agora.")

    def talk(self):
        if self.eating == True:
            print(f"{self.name} não pode falar, pois está comendo.")
        elif self.sleeping == True:
            print(f"{self.name} está falando enquanto dorme.")
        elif self.talking==True:
            print(f"{self.name} já estava falando.")
        else:
            self.talking = True
            print(f"{self.name} está falando agora.")

    def sleep(self):
        if self.talking == True:
            print(f"{self.name} não pode dormir, pois está falando.")
        elif self.eating == True:
            print(f"{self.name} não pode dormir, pois está comendo.")
        elif self.sleeping == True:
            print(f"{self.name} já estava dormindo.")
        else:
            self.sleeping = True
            print(f"{self.name} está dormindo agora.")
    def stopEat(self):
        if self.eating==False:
            print(f"{self.name} já não estava comendo.")
        else:
            self.eating = False
            print(f"{self.name} parou de comer agora.")
    def stopTalk(self):
        if self.talking==False:
            print(f"{self.name} já estava calado.")
        else:
            self.talking = False
            print(f"{self.name} se calou agora.")
    def stopSleep(self):
        if self.sleeping==False:
            print(f"{self.name} já estava acordado.")
        else:
            self.sleeping = False
            print(f"{self.name} acordou agora.")
