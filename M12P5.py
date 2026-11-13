def displayPlayerNames(playerName):
    print()
    print(f"{'Player Name':<15}")
    print("-" * 35)

    for i in range(10):
        print(f"{playerName[i]:<15}")

def displayBattingAverage(battingAverage):
    print()
    print(f"{'Batting Average':>20}")
    print("-" * 35)

    for i in range(10):
        print(f"{battingAverage[i]:>20}")

def displayLastName(lastName):
    print()
    print(f"{'Last Name':<15}")
    print("-" * 35)

    for i in range(10):
        print(f"{lastName[i]:<15}")

playerName = ["Barcenas", "Browere", "Carlson", "Cassaro", "Edstrom", "Hsieh", "James", "Kim", "Ling", "Montes"]

# Example last names list
lastName = playerName

found = False

while not found:
    searchName = input("Enter a player's last name: ")

    if searchName in playerName:
        print(f"{searchName} was found!")
        found = True
    else:
        print("Name is not found. Sorry. :( ")
        print("Please try again.\n")

displayLastName(lastName)