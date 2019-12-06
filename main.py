from replit import clear
import time
import random

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
days = 0
htcount = 0
sellcount = 0
count = htcount + sellcount
assortedanimallist = [" skunks.", " bobcats.", " coyotes.", " racoons.", " possums.", " foxes.", " badgers."]
def nextDay():
  global days
  days += 1
def hunt():
  global skins, htcount, assortedanimalist
  clear()
  print('What do you want to go for?')
  huntanimal  = input('1 for squirrels, 2 for rabbits, and 3 for assorted')
  if huntanimal == "1":
    randomnumber1 = random.randrange(5)
    print('Squirrel Hunting')
    print('You stand in a forest and shoot:')
    print(randomnumber1)
    print('squirrels.')
    skins += randomnumber1
    print('Total skins:')
    print(skins)
  elif huntanimal == "2":
    randomnumber2 = random.randrange(5)
    print('Rabbit Hunting')
    print('You walk for 3 miles and shoot:')
    print(randomnumber2)
    print('rabbits.')
    skins += randomnumber2
    print('Total skins:')
    print(skins)
  elif huntanimal == "3":
    randomnumber3 = random.randrange(3)
    print('Assorted Animal Hunting')
    print('You walk for a few miles and shoot:')
    print(randomnumber3, assortedanimallist[random.randrange(8)])
    skins += randomnumber3
    htcount += 1
    print('Total skins:')
    print(skins)
def trap():
  global htcount, skins, assortedanimallist
  randomnumber4 = random.randrange(traps + 1)
  print('You have')
  print(traps)
  print('traps.')
  print('You set a chain of your traps 1 mile out. You come out later and find ')
  print(randomnumber4)
  print('animals in your ')
  print(traps)
  print('traps.')
  print('You caught')
  print(randomnumber4, assortedanimallist[random.randrange(8)])
  skins += randomnumber4
  htcount += 1
  print('Total skins:')
  print(skins)
def purchase(cost):
  global money
  money = money - cost
  print('Money Balance:')
  print(money)
  print('Thank you for purchasing.')
  time.sleep(2)
def sell():
  global skins, money, sellcount
  money = money + 5
  skins -= 1
  sellcount += 1
  print('Money Balance:')
  print(money)
  print('Skins:')
  print(skins)
  time.sleep(0.6)
def menu():
  clear()
  global money, guns, traps, skins, sellcount, htcount, daysvar, days
  if htcount > 0 and sellcount > 0:
    print("")
  else:
    htcount = 0
    sellcount = 0
    print('Money:')
    print(money)
    print('Guns:')
    print(guns)
    print('Traps:')
    print(traps)
    print('Skins:')
    print(skins)
    menuinput = input('Type 1 to hunt/trap, 2 to go to store, and 3 to sell skins at the market')
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
      elif htcount > 0:
        print('You have already hunted or trapped once today.')
        invalid()
      else:
        htinput = input('Type 1 to hunt and 2 to trap')
        htinput2 = int(input())
        if htinput2 == 1:
          print('Hunt')
          hunt()
          time.sleep(5)
          clear()
          menu()
        elif htinput2 == 2:
          print('Trap')
          trap()
          time.sleep(5)
          clear()
          menu()
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
      elif sellcount > 0:
        print('You have already sold once today.')
        invalid()
      else:
        print('Type 1 to sell all skins.')
        sellvar = input()
        if sellvar == "1":
          while skins > 0:
            sell()
        else:
          invalid()
        print('Thank you for selling.')
        time.sleep(2)
        clear()
        menu()
    else: 
      invalid()
def startGame():
  print("Play this game for as long as you would like. Your money is your score. Use a timer for 5 minutes and beat your or your friend's high score!")
  menu()
startGame()
