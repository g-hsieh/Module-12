def displayPlayers(playerName, battingAverage):
    print()
    print(f"{'Player Name':<15}{'Batting Average':>15}")
    print("-" * 30)

    for i in range(10):
        print(f"{playerName[i]:<15}{battingAverage[i]:>15}")

playerName = ["Barcenas", "Browere", "Carlson", "Cassaro", "Edstrom", "Hsieh", "James", "Kim",
              "Ling", "Montes"]

battingAverage = [8, 12, 2, 25, 10, 13, 5, 6, 7, 14]

found = False

while not found:
    searchName = input("Enter a player's last name: ")

    if searchName in playerName:
        print(f"{searchName} was found!")
        found = True
    else:
        print("Name is not found. Sorry. :( ")
        print("Please try again.\n")

displayPlayers(playerName, battingAverage)