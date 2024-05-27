class Jokenpo:
  def __init__(self, win):
    self.win = win

def move_result(self, name, player, computer):
  if computer == player:
    print("Empate!")
    self.win = False
  elif computer == 'Pedra':
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

  if self.win == False:
    print("COMPUTER WINS!")
  else:
    print(f"{name} WINS!")
