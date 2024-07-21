from collections import defaultdict
class Board : 
  def __init__(self,size) -> None:
    self.start(size)
    self.tie=False

  def start(self,size):

    self.board = [['' for i in range(size)] for j in range(size)]

    self.rows=defaultdict(lambda:defaultdict(int))
    self.columns=defaultdict(lambda:defaultdict(int))
    self.diagonals=defaultdict(lambda:defaultdict(int))
    self.size = size
    self.ct = 0
  def is_tie(self):
    return self.ct == self.size**2
  
  def play(self,player,x,y):
   
     # check if row entry is valid win
    if self.board[x][y] != '':
      raise ValueError("Cell already occupied")
    
    name = player.get_name()

     # fill row
    self.board[x][y] = name

    self.rows[x][name] += 1
    
    if self.rows[x][name] == self.size:
      return True

    self.columns[y][name] += 1

    if self.columns[y][name] == self.size:
      return True
    
    # left to right diagonal
    if x==y:
      self.diagonals[1][name] += 1
      if self.diagonals[1][name] == self.size:
        return True
      
    # right to left diagonal
    if x + y == self.size - 1:
      self.diagonals[2][name] += 1
      if self.diagonals[2][name] == self.size:
        return True
    
    self.ct+=1

    if self.is_tie():
      return True
    
    return False
  
class Player:
  def __init__(self, name):
    self.name = name
  
  def get_name(self):
    return self.name

class Game:
  def __init__(self, player1,player2,board):
      self.player1 = player1
      self.player2 = player2
      self.board = board

  def play(self):

    turn = 1

    while True:

      player = self.player1 if turn == 1 else self.player2

      x = int(input(f'enter player {player.get_name()}`s x coordinate:'))
      print()
      y = int(input(f'enter player {player.get_name()}`s y coordinate:'))
      
      game_end = self.board.play(player,x,y)

      print("-----")

      if game_end:
         
         if self.board.is_tie():
          print("It's a tie")
         else:
          print(f'player {player.get_name()} wins!')

         break
      else:
        turn = 2 if turn == 1 else 1

       

player1 = Player("Bob")
player2 = Player("Alice")
board = Board(3)
game = Game(player1,player2,board)
game.play()



     
  
