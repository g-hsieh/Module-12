def displayarrays(lastName):
    print("Forward Order")
    for x in range(0, 10):
        print(lastName[x])

def rdisplayarrays(lastName):
    print("Reverse Order")

    for i in range(9, -1, -1):
        print(lastName[i])

lastName = ["Adams", "Barcenas", "Browere", "Carlson",
            "Edstrom", "Hsieh", "Jones", "Kim",
            "Lee", "Ling"]

displayarrays(lastName)
rdisplayarrays(lastName)