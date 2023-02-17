#import getpass
import random

opc = ('piedra', 'papel', 'tijeras')
usrPoints = 0
pcPoints = 0

def txt():
  if usr not in range(1,4):
    print('seleccion invalida')
  else:
    print(f"usr: {opc[usr -1]}")
  print(f"pc:  {opc[pc -1]}")

print('Juego de piedra - papel - tijera')

while True:
  usr = int( input('1) piedra, 2) papel, 3)tijera : ') )
  pc = random.randint(1,3)
  
  if pc == usr:
    txt()
    print(f'Empate - PC({pcPoints}) - USR({usrPoints})')
  elif (usr == 1 and pc == 3) or (usr == 2 and pc == 1) or (usr == 3 and pc == 3):
    txt()
    usrPoints += 1
    print(f'Ganaste - PC({pcPoints}) - USR({usrPoints})')
  else:
    txt()
    pcPoints += 1
    print(f'Perdiste - PC({pcPoints}) - USR({usrPoints})')
    

  if pcPoints == 3:
    print(f'**** PC WIN ***** {pcPoints} vs {usrPoints}')
    break
  if usrPoints == 3:
    print(f'**** USER WIN ***** {usrPoints} vs {pcPoints}')
    break

#getpass.getpass('enter')