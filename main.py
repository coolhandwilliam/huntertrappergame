from animations import shootanimation
from replit import clear
import time
import random
import animations
import pickle

def invalid():
  print('Invalid.')
  time.sleep(1)
  clear()
  menu()
print('Hunter/Trapper Game')
try:
    money = pickle.load(open("moneysave.dat", "rb"))
except (OSError, IOError, EOFError) as e:
    money = 100
    pickle.dump(money, open("moneysave.dat", "wb"))
try:
    guns = pickle.load(open("gunsave.dat", "rb"))
except (OSError, IOError, EOFError) as e:
    guns = 0
    pickle.dump(guns, open("gunsave.dat", "wb"))
try:
    traps = pickle.load(open("trapsave.dat", "rb"))
except (OSError, IOError, EOFError) as e:
    traps = 0
    pickle.dump(traps, open("trapsave.dat", "wb"))
try:
    skins = pickle.load(open("skinsave.dat", "rb"))
except (OSError, IOError, EOFError) as e:
    skins = 0
    pickle.dump(skins, open("skinsave.dat", "wb"))
try:
    bigtrap = pickle.load(open("bigtrap.dat", "rb"))
except (OSError, IOError, EOFError) as e:
    bigtrap = 0
    pickle.dump(bigtrap, open("bigtrap.dat", "wb"))
days = 0
htcount = 0
sellcount = 0
count = htcount + sellcount
assortedanimallist = [" skunks.", " bobcats.", " coyotes.", " racoons.", " possums.", " foxes.", " badgers."]
assortedwateranimallist = [" beavers.", " minks.", " otters.", " muskrats."]
assortedbiganimallist = [" deer.", " elk.", " bears.", " antelope."]
try:
    shotgun = pickle.load(open("shotsave.dat", "rb"))
except (OSError, IOError, EOFError) as e:
    shotgun = False
    pickle.dump(shotgun, open("shotsave.dat", "wb"))
try:
    watertrap = pickle.load(open("watertrap.dat", "rb"))
except (OSError, IOError, EOFError) as e:
    watertrap = False
    pickle.dump(watertrap, open("watertrap.dat", "wb"))
try:
    watertrap = pickle.load(open("watertrap.dat", "rb"))
except (OSError, IOError, EOFError) as e:
    watertrap = False
    pickle.dump(watertrap, open("watertrap.dat", "wb"))
def nextDay():
  global days
  days += 1
def shotgunhunt(nameofanimal):
  shootanimation()
  randomnumber7 = random.randrange(10)
  print(nameofanimal,' Hunting')
  print('You walk for a few miles and shoot:')
  print(randomnumber7, ' ', nameofanimal, 's.')
  skins = skins + randomnumber7 * 2
  print('Total skins:')
  print(skins)
def hunt():
  global skins, htcount, assortedanimalist
  clear()
  print('What do you want to go for?')
  huntanimal  = input('1 for squirrels, 2 for rabbits, and 3 for assorted')
  if huntanimal == "1":
    shootanimation()
    randomnumber1 = random.randrange(5)
    if shotgun == True:
      shotgunhunt('squirrel')
    else:
      randomnumber1 = random.randrange(5)
      shootanimation()
      print('Squirrel Hunting')
      print('You stand in a forest and shoot:')
      print(randomnumber1)
      print('squirrels.')
      skins += randomnumber1 
      print('Total skins:')
      print(skins)
  elif huntanimal == "2":
    shootanimation()
    randomnumber2 = random.randrange(10)
    if shotgun == True:
      shotgunhunt('rabbit')
    else:
      randomnumber2 = random.randrange(5)
      shootanimation()
      print('Rabbit Hunting')
      print('You walk for 3 miles and shoot:')
      print(randomnumber2)
      print('rabbits.')
      skins += randomnumber2
      print('Total skins:')
      print(skins)
  elif huntanimal == "3":
    if shotgun == True:
      shotgunhunt('assorted animal')
    else:
      shootanimation()
      randomnumber3 = random.randrange(3)
      print('Assorted Animal Hunting')
      print('You walk for a few miles and shoot:')
      print(randomnumber3, assortedanimallist[random.randrange(7)])
      skins += randomnumber3
      htcount += 1
      print('Total skins:')
      print(skins)
  else:
    invalid()
def trap():
  shootanimation()
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
  print(randomnumber4, assortedanimallist[random.randrange(7)])
  skins += randomnumber4
  htcount += 1
  print('Total skins:')
  print(skins)
def watertrap1():
  shootanimation()
  global htcount, skins, assortedwateranimallist
  randomnumber5 = random.randrange(traps + 2)
  print('You have')
  print(traps)
  print('traps.')
  print('You set a water trap in a stream as well. You come out later and find ')
  print(randomnumber5)
  print('animals in your water trap.')
  print('You caught')
  print(randomnumber5, assortedwateranimallist[random.randrange(4)])
  skins += randomnumber5 * 2
  htcount += 1
  print('Total skins:')
  print(skins)
def bigtrap1():
  global bigtrap
  shootanimation()
  global htcount, skins, assortedbiganimallist
  randomnumber6 = random.randrange(2)
  print('You have')
  print(traps)
  print('traps.')
  print('You set a big game trap in a field as well. You come out later and find ')
  print(randomnumber6)
  print('animals in your water trap.')
  print('You caught')
  print(randomnumber6, assortedbiganimallist[random.randrange(4)])
  skins += randomnumber6 * 5
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
def savequit():
  print('Saving...')
  open("moneysave.dat", "w").close()
  open("gunsave.dat", "w").close()
  open("trapsave.dat", "w").close()
  open("skinsave.dat", "w").close()
  open("shotsave.dat", "w").close()
  open("watertrap.dat", "w").close()
  pickle.dump(money, open("moneysave.dat", "wb"))
  pickle.dump(guns, open("gunsave.dat", "wb"))
  pickle.dump(traps, open("trapsave.dat", "wb"))
  pickle.dump(skins, open("skinsave.dat", "wb"))
  pickle.dump(shotgun, open("shotsave.dat", "wb"))
  pickle.dump(watertrap, open("watertrap.dat", "wb"))
  print('Done saving.')
  print('Quitting...')
  quit()
def menu():
  clear()
  global money, guns, traps, skins, sellcount, htcount, daysvar, days, shotgun, watertrap, bigtrap
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
    menuinput = input('Type 1 to hunt/trap, 2 to go to store, 3 to sell skins at the market, and 4 to save and quit')
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
        print('Type 1 to hunt and 2 to trap')
        htinput2 = input()
        if htinput2 == "1":
          print('Hunt')
          hunt()
          time.sleep(5)
          clear()
          menu()
        elif htinput2 == "2":
          if watertrap == True and bigtrap == 0:
            print('Trap and Watertrap')
            trap()
            time.sleep(3)
            watertrap1()
            time.sleep(3)
            clear()
            menu()
          elif watertrap == True and bigtrap == 1:
            print('Trap and Watertrap and Big Game Trap')
            trap()
            time.sleep(3)
            watertrap1()
            time.sleep(3)
            bigtrap1()
            time.sleep(3)
            clear()
            menu()
          elif bigtrap == 1 and watertrap == False:
            print('Trap and Watertrap')
            trap()
            time.sleep(3)
            bigtrap1()
            time.sleep(3)
            clear()
            menu()
          else:
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
          print('Type 1 to buy a rifle (60 coins) or 2 to buy a shotgun(1000 coins)(major benefits)')
          gunpurchase1 = input()
          if gunpurchase1 == "1":
            purchase(60)
            guns += 1
            clear()
            menu()
          elif gunpurchase1 == "2":
            purchase(1000)
            guns += 1
            clear()
            menu()
            shotgun = True
          else: 
            invalid()
        elif storetype1 == "2":
          print('TRAPS')
          print('Type 1 to purchase a trap/snare(10),type 2 to purchase a water snare(1500), and type 3 to purchase a big game trap(3000)')
          entervar = input()
          if entervar == "1":
            purchase(10)
            traps += 1
            clear()
            menu()
          elif entervar == "2":
            purchase(1500)
            watertrap = True
            clear()
            menu()
          elif entervar == "3":
            purchase(3000)
            bigtrap = 1
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
    elif menuinput == "4":
      savequit()
    else: 
      invalid()
x = 0
def startGame():
  global x
  time.sleep(1)
  while x < 5:
    shootanimation()
    x+=1
  print("Play this game for as long as you would like. Your money is your score. Use a timer for 5 minutes and beat your or your friend's high score!")
  time.sleep(2)
  menu()
startGame()
