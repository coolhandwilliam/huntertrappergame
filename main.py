from replit import clear
import time

def invalid():
  print('Invalid.')
  time.sleep(1)
  clear()
  menu()
print('Hunter/Trapper Game')
money = 100
guns = 0
traps = 0
skins = 0
def purchase(cost):
  global money
  money = money - cost
  print('Money Balance:')
  print(money)
  print('Thank you for purchasing.')
  time.sleep(2)
def menu():
  global money, guns, traps, skins
  print('Money:')
  print(money)
  print('Guns:')
  print(guns)
  print('Traps:')
  print(traps)
  print('Skins:')
  print(skins)
  menuinput = input('Type 1 to hunt/trap, 2 to go to store, and 3 to sell hides at the market')
  if menuinput == "1":
    clear()
    print('Guns:')
    print(guns)
    print('Traps:')
    print(traps)
    if traps < 1 and guns < 1:
      time.sleep(2)
      clear()
      print('Sorry, you have no guns or traps.')
      menu()
    else:
      htinput = input('Type 1 to hunt and 2 to trap')
      htinput2 = input()
      if htinput2 == "1":
        print('Hunt')
      elif htinput2 == "2":
        print('Trap')
      else:
        invalid()
  elif menuinput == "2":
    clear()
    print('STORE')
    print('Money:')
    print(money)
    if money < 1:
      time.sleep(1)
      clear()
      print('Sorry, you have no money. Sell some skins to make some!')
      menu()
    else:
      print('Type 1 to look at guns')
      print('Type 2 to look at traps')
      storetype1 = input()
      if storetype1 == "1":
        print('GUNS')
        print('Type 1 to buy a rifle (60 coins).')
        gunpurchase1 = input()
        if gunpurchase1 == "1":
          purchase(60)
          guns += 1
          clear()
          menu()
        else: 
          invalid()
      elif storetype1 == "2":
        print('TRAPS')
        print('Type 1 to purchase a trap/snare(10)')
        entervar = input()
        if entervar == "1":
          purchase(10)
          traps += 1
          clear()
          menu()
        else:
          invalid()
      else:
        invalid()
  elif menuinput == "3":
    clear()
    print('Skins:')
    print(skins)
    if skins < 1:
      print('Sorry, you own no skins. Hunt and trap to get some!')
      time.sleep(2)
      clear()
      menu()
  else:
    invalid()
def startGame():
  menu()
startGame()
