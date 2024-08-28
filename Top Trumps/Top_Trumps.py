import random as r  # Importing the random module to shuffle the deck
import time as t    # Importing the time module to add delays for better gameplay experience
import sys          # Importing the sys module to use system-specific functions
import os           # Importing the os module to interact with the operating system

# Get and print the current working directory (for file path references)
cwd = os.getcwd()
print(cwd)
input("Stop!")  # Pauses the program until the user presses Enter

# Define the Card class, which represents each card in the game
class card():
    def __init__(self, Individual, Owners, Size, Speed, FirePower, Maneuvering, ForceFactor):
        # Initializing attributes for the card, like the ship's name, owner, and stats
        self.Individual = Individual
        self.Owners = Owners
        self.Size = Size
        self.Speed = Speed
        self.FirePower = FirePower
        self.Maneuvering = Maneuvering
        self.ForceFactor = ForceFactor
    
    # Method to print the details of the card in a readable format
    def printcard(self):
        print(f"{self.Individual} flown by {self.Owners}")
        print(f"Size: {self.Size}")
        print(f"Speed: {self.Speed}")
        print(f"Fire Power: {self.FirePower}")
        print(f"Maneuvering: {self.Maneuvering}")
        print(f"Force Factor: {self.ForceFactor}")
        print()
    
    # Method to return the stats of the card as a list
    def returnstats(self):
        return [self.Size, self.Speed, self.FirePower, self.Maneuvering, self.ForceFactor]

# Define the Pile class, which represents a collection of cards (like a deck)
class pile():
    def __init__ (self):
        # Initialize a pile of 40 empty cards, simulating a circular queue
        self.cards = [card("", "", 0, 0, 0, 0, 0) for i in range(40)]
        self.size = 40
        self.sp = 0  # Start pointer
        self.ep = -1 # End pointer, initialized to -1 (this will cause issues)
        self.cardamount = 0  # Number of cards currently in the pile
    
    # Method to add a card to the pile
    def addcard(self, card):
        if self.cardamount != 40:  # Ensure the pile isn't full
            self.cardamount += 1
            self.ep += 1  # Move the end pointer to the next position
            if self.ep > 39:  # If end pointer exceeds the pile size, wrap around
                self.ep = 0
            self.cards[self.ep] = card  # Place the card in the pile
        else:
            print("Pile is full")
    
    # Method to remove a card from the pile
    def removecard(self):
        if self.cardamount != 0:  # Ensure there are cards to remove
            self.cardamount -= 1
            thiscard = self.cards[self.sp]
            self.sp += 1  # Move the start pointer to the next card
            if self.sp > 39:  # If start pointer exceeds the pile size, wrap around
                self.sp = 0
            return thiscard
        else:
            print("No Cards!")
    
    # Method to print all the cards currently in the pile
    def mainprint(self):
        index = self.sp  # Start printing from the start pointer
        if self.cardamount != 0:  # Ensure there are cards to print
            if self.ep == 39:
                self.stop = 0  # Stop printing at the wrapped-around end
            else:
                self.stop = self.ep + 1  # Stop printing at the actual end
            while index != self.stop:  # Continue printing until reaching the stop point
                self.cards[index].printcard()
                if index == 40:
                    index == 0  # Wrap around the index if it exceeds pile size
                else:
                    index += 1
        else:
            print("No Cards")
    
    # Method to add cards from a file (e.g., a CSV file with card data)
    def addfromfile(self, file):
        try:
            myFile = open(f"./Top Trumps/{file}", "r")
            for i, j in enumerate(myFile):
                elements = j.strip().split(",")  # Split each line into elements
                if i > 0:  # Skip the header line
                    self.addcard(card(elements[0], elements[1], int(elements[2]), int(elements[3]), int(elements[4]), int(elements[5]), int(elements[6])))
        except:
            print("No file Called That")
    
    # Method to shuffle the cards in the pile
    def shuffle(self):
        r.shuffle(self.cards)  # Randomly shuffle the cards
        self.temparray = []
        for i in self.cards:
            if i.Individual == "":
                self.temparray.append(i)  # Collect empty cards
            else:
                self.temparray.insert(0, i)  # Collect non-empty cards
        self.cards = self.temparray  # Reassign the shuffled cards to the pile
    
    # Method to print the raw data of each card in the pile (for debugging)
    def dirtyprint(self):
        for i in self.cards:
            print(vars(i))

# Function to clear the terminal screen (works on both Windows and Unix-based systems)
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to handle a player's turn
def turn(Player_No: int, Opp_No: int, PlayerCard: card, OppCard: card):
    playerstats = PlayerCard.returnstats()
    Oppstats = OppCard.returnstats()
    choices = ["Size", "Speed", "Fire Power", "Maneuvering", "Force Factor"]
    
    # Display player's card with a simulated dealing effect
    sys.stdout.write(f"Dealing Player {Player_No}'s Card")
    for i in range(5):
        sys.stdout.write(".")
        sys.stdout.flush()
        t.sleep(.5)
    print()
    PlayerCard.printcard()
    
    # Show the available stat choices
    print("1. Size")
    print("2. Speed")
    print("3. Fire Power")
    print("4. Maneuvering")
    print("5. Force Factor")
    print()
    
    # Get the player's choice of stat
    choice = "z"
    while choice not in ["1", "2", "3", "4", "5"]:
        choice = input("Enter the number corresponding to your choice: ")
    choice = int(choice) - 1
    print(f"You chose {choices[choice]} at {playerstats[choice]}")
    
    # Display opponent's card with a simulated dealing effect
    sys.stdout.write(f"Dealing Player {Opp_No}'s Card")
    for i in range(5):
        sys.stdout.write(".")
        sys.stdout.flush()
        t.sleep(.5)
    print()
    OppCard.printcard()
    
    # Compare the selected stat and determine the winner of the round
    if (playerstats[choice] > Oppstats[choice] and Player_No == 1) or (Oppstats[choice] > playerstats[choice] and Player_No == 2):
        print(f"Player 1 Wins {2 + table.cardamount} cards")
        if Player_No == 1:
            player1.addcard(PlayerCard)
            player1.addcard(OppCard)
        if table.cardamount > 0:
            for i in range(table.cardamount):
                player1.addcard(table.removecard())
    elif (playerstats[choice] < Oppstats[choice] and Player_No == 1) or (Oppstats[choice] < playerstats[choice] and Player_No == 2):
        print(f"Player 2 Wins {2 + table.cardamount} cards")
        player2.addcard(PlayerCard)
        player2.addcard(OppCard)
        if table.cardamount > 0:
            for i in range(table.cardamount):
                player1.addcard(table.removecard())
    else:
        # If it's a draw, the cards go to the table
        table.addcard(PlayerCard)
        table.addcard(OppCard)
        print(f"It's a draw - There are now {table.cardamount} cards on the Table!")
    
    input("Press Enter to continue...")
    print()
    print("*******************************************************")

# Main function to run the game
def maingame():
    print("Starting the main game...")
    global allcards, player1, player2, table
    allcards = pile()  # Initialize a pile for all cards
    player1 = pile()  # Initialize a pile for player 1
    player2 = pile()  # Initialize a pile for player 2
    table = pile()  # Initialize a pile for the table
    
    allcards.addfromfile("TopTrumps-StarWarsStarshipsR.csv")  # Load the cards from a file
    allcards.shuffle()  # Shuffle the deck
    
    player1sturn = True  # Variable to track whose turn it is
    for i in range(int(allcards.cardamount / 2)):
        player1.addcard(allcards.removecard())  # Distribute half of the cards to player 1
        player2.addcard(allcards.removecard())  # Distribute the other half of the cards to player 2
    
    # The main game loop continues until one player runs out of cards
    while (player1.cardamount != 0) and (player2.cardamount != 0):
        print()
        print(f"Player 1 has {player1.cardamount} cards left")
        print(f"Player 2 has {player2.cardamount} cards left")
        print(f"There are {table.cardamount} cards on the table")
        print()
        
        # Each player draws a card from their respective piles
        player1card = player1.removecard()
        player2card = player2.removecard()
        
        # Retrieve and print the stats of the drawn cards (for debugging purposes)
        player1stats = player1card.returnstats()
        player2stats = player2card.returnstats()
        print(player1stats, player2stats)
        
        # Determine whose turn it is
        if player1sturn:
            turn(1, 2, player1card, player2card)  # Player 1's turn
            player1sturn = False  # Switch turn to Player 2
        else:
            turn(2, 1, player2card, player1card)  # Player 2's turn
            player1sturn = True  # Switch turn to Player 1
        
        print()
        print("*******************************************************")
    
    # After the loop, check which player has run out of cards and declare the winner
    if player1.cardamount == 0:
        print("Player 2 Wins")  # Player 2 wins if Player 1 has no cards left
    else:
        print("Player 1 Wins")  # Player 1 wins if Player 2 has no cards left

# Function to display the game introduction and handle the initial menu
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
    
    # Loop to ensure the user enters a valid input to start or quit the game
    while True:
        choice = input("Press 1 to start, Press 0 to quit: ")
        if choice == "1":
            clear_terminal()  # Clear the terminal screen before starting the game
            maingame()  # Start the main game
            break
        elif choice == "0":
            print("Quitting the game...")
            break  # Exit the loop and quit the game
        else:
            print("Invalid input. Please enter 1 to start or 0 to quit.")

# Start the game by calling the game_intro function
game_intro()