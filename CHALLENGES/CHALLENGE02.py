class Jokenpo:
    def __init__(self, win):
        self.win = win

    def move_result(self, computer, player, name):
        if computer == player:
            print("Empate!")
        else:
            if computer == 'Pedra':
                if player == 'Papel':
                    self.win = True
                elif player == 'Tesoura':
                    self.win = False
            elif computer == 'Papel':
                if player == 'Tesoura':
                    self.win = True
                elif player == 'Pedra':
                    self.win = False
            elif computer == 'Tesoura':
                if player == 'Pedra':
                    self.win = True
                elif player == 'Papel':
                    self.win = False

            if self.win:
                print("COMPUTER WINS!")
            else:
                print(f"{name} WINS!")
