from animations import shootanimation
from replit import clear
import time
import random
import animations
import pickle
from instructions import instructions

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
rifleammo = 0
shotgunshells = 0
rifle = False
shotgun = 0
trapbait = 0
try:
    watertrap = pickle.load(open("watertrap.dat", "rb"))
except (OSError, IOError, EOFError) as e:
    watertrap = False
    pickle.dump(watertrap, open("watertrap.dat", "wb"))
def hunt():
  global skins, htcount, assortedanimalist, rifle, rifleammo, shotgun, shotgunshells
  clear()
  if guns < 1:
    print('No guns.')
    time.sleep(1)
    invalid()
  else:
    print('What do you want to go for?')
    huntanimal  = input('1 for squirrels, 2 for rabbits, and 3 for assorted')
    if rifleammo < 1 and shotgunshells < 1:
      print('No ammo.')
      time.sleep(1)
      invalid()
    else:
      if huntanimal == "1":
        if rifle == True:
          randomnumber1 = random.randrange(rifleammo + 1)
          shootanimation()
          print('Squirrel Hunting')
          print('You stand in a forest and shoot: ', randomnumber1, 'squirrels.')
          skins += randomnumber1 
          print('Total skins:')
          print(skins)
          rifleammo -= randomnumber1
        elif shotgun == 1:
          randomnumber1 = random.randrange(shotgunshells + 1)
          shootanimation()
          print('Squirrel Hunting')
          print('You stand in a forest and shoot: ', randomnumber1, 'squirrels.')
          skins += randomnumber1 
          print('Total skins:')
          print(skins)
          shotgunshells -= randomnumber1
        else:
          print('No guns.')
          print('Redirecting...')
          time.sleep(1)
          clear()
          menu()
      if huntanimal == "2":
        if rifle == True:
          randomnumber2 = random.randrange(rifleammo + 1)
          shootanimation()
          print('Rabbit Hunting')
          print('You stand in a forest and shoot: ', randomnumber2, 'rabbits.')
          skins += randomnumber2 
          print('Total skins:')
          print(skins)
          rifleammo -= randomnumber2
        elif shotgun == 1:
          randomnumber2 = random.randrange(shotgunshells + 1)
          shootanimation()
          print('Rabbit Hunting')
          print('You stand in a forest and shoot: ', randomnumber2, 'rabbits.')
          skins += randomnumber2 
          print('Total skins:')
          print(skins)
          shotgunshells -= randomnumber2
        else:
          print('No guns.')
          print('Redirecting...')
          time.sleep(1)
          clear()
          menu()  
      if huntanimal == "3":
        if rifle == True:
          randomnumber3 = random.randrange(rifleammo + 1)
          shootanimation()
          print('Assorted Animal Hunting')
          print('You stand in a forest and shoot: ', randomnumber3, assortedanimallist[random.randrange(7)])
          skins += randomnumber3 
          print('Total skins:')
          print(skins)
          rifleammo -= randomnumber3
        elif shotgun == 1:
          randomnumber3 = random.randrange(shotgunshells + 1)
          shootanimation()
          print('Assorted Animal Hunting')
          print('You stand in a forest and shoot: ', randomnumber3, assortedanimallist[random.randrange(7)])
          skins += randomnumber3 
          print('Total skins:')
          print(skins)
          shotgunshells -= randomnumber3 
def trap():
  global traps, trapbait, skins, assortedanimallist
  if traps < 1:
    print('No traps')
    invalid()
  else:
    if trapbait < 1:
      print('No bait.')
      invalid()
    else:
      shootanimation()
      randomnumber4 = random.randrange(trapbait + 1)
      print('You have', traps, 'traps and ', trapbait, 'bait.')
      print('You set a chain of your baited traps 1 mile out. You come out later and find ')
      print(randomnumber4)
      print('animals in your ')
      print(traps)
      print('traps.')
      print('You caught')
      print(randomnumber4, assortedanimallist[random.randrange(7)])
      skins += randomnumber4
      trapbait -= randomnumber4
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
  print('Total skins:')
  print(skins)
def purchase(cost):
  global money
  if(cost > money):
    print('Not enough money. Redirecting to menu.')
    time.sleep(1)
    clear()
    menu()
  else:
    money = money - cost
    print('Money Balance:')
    print(money)
    print('Thank you for purchasing.')
def sell():
  global skins, money, sellcount
  money = money + 5
  skins -= 1
  sellcount += 1
  print('Money Balance:')
  print(money)
  print('Skins:')
  print(skins)
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
  global money, guns, traps, skins, sellcount, htcount, daysvar, days, shotgun, watertrap, bigtrap, rifleammo, shotgunshells, rifle, shotgun, trapbait
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
    print('Shotgun Shells:')
    print(shotgunshells)
    print('Rifle Ammo:')
    print(rifleammo)
    print('Trap Bait:')
    print(trapbait)
    print('')
    menuinput = input('Type 1 to hunt/trap, 2 to go to store, 3 to sell skins at the market, and 4 to view instructions')
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
        print('Type 1 to look at guns and ammo')
        print('Type 2 to look at traps and trap bait')
        storetype1 = input()
        if storetype1 == "1":
          print('GUNS AND AMMO')
          print('Type 1 to buy a rifle (60 coins), 2 to buy a shotgun(70 coins)(cheaper shells), and 3 to view shells.')
          gunpurchase1 = input()
          if gunpurchase1 == "1":
            purchase(60)
            rifle = True
            guns += 1
            clear()
            menu()
          elif gunpurchase1 == "2":
            purchase(70)
            guns += 1
            shotgun = 1
            clear()
            menu()
          elif gunpurchase1 == "3":
            print('Type 1 to buy rifle ammunition(2) and 2 to buy shotgun shells(1)')
            ammopurchase1 = input()
            if ammopurchase1 == "1":
              print('How many do you want to buy?')
              quantity = int(input())
              while quantity > 0:
                purchase(2)
                quantity -= 1
                rifleammo += 1
              clear()
              menu()
            elif ammopurchase1 == "2":
              print('How many do you want to buy?')
              quantity = int(input())
              while quantity > 0:
                purchase(1)
                quantity -= 1
                shotgunshells += 1
              clear()
              menu()
          else: 
            invalid()
        elif storetype1 == "2":
          print('TRAPS')
          print('Type 1 to purchase a trap/snare(10),type 2 to purchase a water snare(1500), type 3 to purchase a big game trap(3000), and type 4 to purchase bait for one trap(4)(no bait required for big game trap and water snare)')
          entervar = input()
          if entervar == "1":
            print('How many do you want to buy?')
            quantity = int(input())
            while quantity > 0:
              purchase(10)
              quantity -= 1
              traps += 1
            clear()
            menu()
          elif entervar == "2":
            print('How many do you want to buy?')
            quantity = int(input())
            while quantity > 0:
              purchase(1500)
              quantity -= 1
              watertrap = True
            clear()
            menu()
          elif entervar == "3":
            print('How many do you want to buy?')
            quantity = int(input())
            while quantity > 0:
              purchase(3000)
              quantity -= 1
              bigtrap += 1
            clear()
            menu()
          elif entervar == "4":
            print('How many do you want to buy?')
            quantity = int(input())
            while quantity > 0:
              purchase(4)
              quantity -= 1
              trapbait += 1
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
        print('Type 1 to sell all skins.')
        sellvar = input()
        if sellvar == "1":
          while skins > 0:
            sell()
          time.sleep(2)
        else:
          invalid()
        print('Thank you for selling.')
        time.sleep(2)
        clear()
        menu()
    elif menuinput == "4":
      instructions()
      print('Press enter to continue')
      entervar2 = input()
      clear()
      menu()
    else: 
      invalid()
x = 0
def startGame():
  global x
  time.sleep(1)
  while x < 5:
    shootanimation()
    x+=1
  menu()
startGame()
