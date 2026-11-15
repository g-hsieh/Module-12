from pathlib import Path

def displayPlayers(playerName, battingAverage):
    print()
    print(f"{'Player Name':<15}{'Batting Average':>15}")
    print("-" * 30)

    for i in range(len(playerName)):
        print(f"{playerName[i]:<15}{battingAverage[i]:>15.3f}")


def searchName(searchPlayer, playerName):

    for i in range(len(playerName)):
        if playerName[i].lower() == searchPlayer.lower():
            return i

    return -1


# Read names
M12P4_names = Path("/Users/gracehsieh/CIS 106:VS Python/Module 12/M12P4_lastnames")

# Read batting averages
M12P4_avg = Path("/Users/gracehsieh/CIS 106:VS Python/Module 12/M12P4_battingAvg")

playerName = []
battingAverage = []

# Read names
if M12P4_names.exists():
    with open(M12P4_names, "r") as infile:
        for line in infile:
            playerName.append(line.strip())

# Read batting averages
if M12P4_avg.exists():
    with open(M12P4_avg, "r") as infile:
        for line in infile:
            battingAverage.append(float(line.strip()))

# Display data
displayPlayers(playerName, battingAverage)

# First search
searchLastName = input("\nEnter a player's last name: ")

i = searchName(searchLastName, playerName)

if i == -1:
    print(searchLastName, "is not in the array")
else:
    print()
    print(f"Player Name: {playerName[i]}")
    print(f"Batting Average: {battingAverage[i]:.3f}")

# While loop searches
response = input("\nWould you like to enter another player's last name? (YES/NO): ")

while response.upper() == "YES":

    searchLastName = input("Enter a player's last name: ")

    i = searchName(searchLastName, playerName)

    if i == -1:
        print(searchLastName, "is not in the array")
    else:
        print()
        print(f"Player Name: {playerName[i]}")
        print(f"Batting Average: {battingAverage[i]:.3f}")

    response = input(
        "\nWould you like to enter another player's last name? (YES/NO): "
    )

print("\nHave a nice day.")