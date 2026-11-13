def displayarrays(lastName, examScore):
    print()
    print("Forward Order")
    print()
    print(f"{'last Name':<15}{'Exam Score':>12}")
    print("-" * 29)

    for i in range(0, 10):
        print(f"{lastName[i]:<15}{examScore[i]:>12}")

def rdisplay(lastName, examScore):
    print()
    print("Reverse Order")
    print()
    print(f"{'Last Name':<15}{'Exam Score':>12}")
    print("-" * 29)

    for i in range(9, -1, -1):
        print(f"{lastName[i]:<15}{examScore[i]:>12}")

lastName = ["Adams", "Barcenas", "Browere", "Carlson",
            "Edstrom", "Hsieh", "Jones", "Kim",
            "Lee", "Ling"]

examScore = ["80", "84", "89", "90", "92",
             "95", "100", "110", "122", "150"]

displayarrays(lastName, examScore)
rdisplay(lastName, examScore)