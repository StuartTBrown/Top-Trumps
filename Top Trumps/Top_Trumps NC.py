
import random as r
import time as t
import sys


class card():
    def __init__(self,Individual,Owners,Size,Speed,FirePower,Maneuvering,ForceFactor):
        self.Individual = Individual
        self.Owners = Owners
        self.Size = Size
        self.Speed = Speed
        self.FirePower = FirePower
        self.Maneuvering = Maneuvering
        self.ForceFactor = ForceFactor
    def printcard(self):
        print (f"{self.Individual} flown by {self.Owners}")
        print (f"Size: {self.Size}")
        print (f"Speed: {self.Speed}")
        print (f"Fire Power: {self.FirePower}")
        print (f"Maneuvering: {self.Maneuvering}")
        print (f"Force Factor: {self.ForceFactor}")
        print ()
    def returnstats(self):
        return [self.Size,self.Speed,self.FirePower,self.Maneuvering,self.ForceFactor]

class pile():
    def __init__ (self):
        # lets implement it as a Circular Queue size 40
        self.cards = [card("","",0,0,0,0,0) for i in range (40)]
        self.size = 40
        self.sp = 0
        self.ep = -1 # point out my mistake here!
        self.cardamount = 0
    def addcard(self,card):
        if self.cardamount != 40:
            self.cardamount +=1
            self.ep += 1
            #print(self.ep)
            if self.ep > 39:
                self.ep = 0
            self.cards[self.ep] = card
            
            
        else:
            print("Pile is full")
    def removecard(self):
        if self.cardamount != 0:
            self.cardamount -=1
            thiscard = self.cards[self.sp]
            self.sp +=1
            if self.sp > 39:
                self.sp = 0
            return thiscard
        else:
            print("No Cards!")
    def mainprint(self):
        index = self.sp
        if self.cardamount !=0:
            if self.ep == 39:
                self.stop = 0
            else:
                self.stop = self.ep +1 
            while index!=self.stop:
                self.cards[index].printcard()
                if index == 40:
                    index == 0
                else:
                    index +=1
        else:
            print("No Cards")
            
    def addfromfile(self,file):
        try:
            myFile = open(file, "r")
            for i,j in enumerate(myFile):
                elements = j.strip().split(",")
                if i > 0:
                    self.addcard(card(elements[0],elements[1],int(elements[2]),int(elements[3]),int(elements[4]),int(elements[5]),int(elements[6])))
                    
        except: 
            print("No file Called That")
            
    def shuffle(self):
        r.shuffle(self.cards)
        self.temparray = []
        for i in self.cards:
            if i.Individual == "":
                self.temparray.append(i)
            else:
                self.temparray.insert(0,i)
        self.cards = self.temparray
    
    def dirtyprint(self):
        for i in self.cards:
            print(vars(i))
                
        
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def turn(Player_No: int,Opp_No: int,PlayerCard: card,OppCard: card):
    playerstats = PlayerCard.returnstats()
    Oppstats = OppCard.returnstats()
    choices = ["Size","Speed","Fire Power","Maneuvering","Force Factor"]
    print()
    sys.stdout.write(f"Dealing Player {Player_No}'s Card")
    for i in range(5):                
        sys.stdout.write(".")
        sys.stdout.flush()
        t.sleep(.5)
    print()
    print()
    PlayerCard.printcard()
    print("1. Size")
    print("2. Speed")
    print("3. Fire Power")
    print("4. Maneuvering")
    print("5. Force Factor")
    print()
    choice = "z"
    while choice not in ["1", "2", "3", "4", "5"]:
        choice = input("Enter the number corresponding to your choice: ")
    choice = int(choice)-1
    print()
    print(f"You chose {choices[choice]} at {playerstats[choice]}")
    print()
    sys.stdout.write(f"Dealing Player {Opp_No}'s Card")
    for i in range(5):                
        sys.stdout.write(".")
        sys.stdout.flush()
        t.sleep(.5)
    print()
    print()
    OppCard.printcard()
    print(f"Player 1's {choices[choice]} is {playerstats[choice]} Player 2's {choices[choice]} is {Oppstats[choice]}")
    if (playerstats[choice] > Oppstats[choice] and Player_No == 1) or (Oppstats[choice] > playerstats[choice] and Player_No == 2):
        print(f"Player 1 Wins {2+table.cardamount} cards")
        if Player_No == 1:
            player1.addcard(PlayerCard)
            player1.addcard(OppCard)
        if table.cardamount > 0:
            for i in range(table.cardamount):
                player1.addcard(table.removecard())
    elif (playerstats[choice] < Oppstats[choice] and Player_No == 1) or (Oppstats[choice] < playerstats[choice] and Player_No == 2):
        print(f"Player 2 Wins {2+table.cardamount} cards")
        player2.addcard(PlayerCard)
        player2.addcard(OppCard)
        if table.cardamount > 0:
            for i in range(table.cardamount):
                player1.addcard(table.removecard())
    else:
        table.addcard(PlayerCard)
        table.addcard(OppCard)
        print(f"It's a draw - There are now {table.cardamount} cards on the Table!")
    input("Press Enter to continue...")
    print ()
    print ("*******************************************************")
    

def maingame():
    print("Starting the main game...")
    global allcards,player1,player2,table
    allcards = pile()
    player1 = pile()
    player2 = pile()
    table = pile()
    allcards.addfromfile("TopTrumps-StarWarsStarshipsR.csv")
    allcards.shuffle()
    #playerturn = 1
    player1sturn = True
    for i in range(int(allcards.cardamount/2)):
        player1.addcard(allcards.removecard())
        player2.addcard(allcards.removecard())
    while (player1.cardamount != 0) and (player2.cardamount != 0):
        print()
        print(f"Player 1 has {player1.cardamount} cards left")
        print(f"Player 2 has {player2.cardamount} cards left")
        print(f"There are {table.cardamount} cards on the table")
        print()
        
        player1card = player1.removecard()
        player2card = player2.removecard()
        choices = ["Size","Speed","Fire Power","Maneuvering","Force Factor"]
        player1stats = player1card.returnstats()
        player2stats = player2card.returnstats()
        print (player1stats,player2stats)
        
        if player1sturn:
            turn(1,2,player1card,player2card)
            player1sturn = False
        else:
            turn(2,1,player2card,player1card)
            player1sturn = True
            print ()
            print ("*******************************************************")
    if player1.cardamount == 0:
        print ("Player 2 Wins")
    else:
        print ("Player 1 Wins")       
            #break
            


def game_intro():
    print(r"""
      _________ __                  __      __                           
     /   _____//  |______ _______  /  \    /  \_____ _______  ______     
    \_____  \\   __\__  \\_  __ \ \   \/\/   /\__  \\_  __ \/  ___/     
    /        \|  |  / __ \|  | \/  \        /  / __ \|  | \/\___ \      
    /_______  /|__| (____  /__|      \__/\  /  (____  /__|  /____  >     
            \/           \/               \/        \/           \/      
    ___________             ___________                                  
    \__    ___/___ ______   \__    ___/______ __ __  _____ ______  ______
    |    | /  _ \\____ \    |    |  \_  __ \  |  \/     \\____ \/  ___/
    |    |(  <_> )  |_> >   |    |   |  | \/  |  /  Y Y  \  |_> >___ \ 
    |____| \____/|   __/    |____|   |__|  |____/|__|_|  /   __/____  >
                  |__|                                  \/|__|       \/ 
                            A Game by Stuart Brown
    """)
    
    while True:
        choice = input("Press 1 to start, Press 0 to quit: ")
        if choice == "1":
            clear_terminal()
            maingame()
            break
        elif choice == "0":
            print("Quitting the game...")
            break
        else:
            print("Invalid input. Please enter 1 to start or 0 to quit.")


game_intro()          
                      
            




            
    
    
    
    

