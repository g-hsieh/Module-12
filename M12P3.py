def displayExam(lastName, ExamScore):
    print()
    print("Sorted by Lowest Score")
    print(f"{'Last Name':<15}{'Exam Score':>12}")
    print("-" * 27)

    for i in range(0, 10):
        print(f"{lastName[i]:<15}{ExamScore[i]:>12}")

def rdisplay(lastName, ExamScore):
    print()
    print("Sorted by Highest Score")
    print(f"{'Last Name':<15}{'Exam Score':>12}")
    print("-" * 27)

    for i in range(9, -1, -1):
        print(f"{lastName[i]:<15}{ExamScore[i]:>12}")

def hilow(lastName, ExamScore):

    l = len(lastName)

    for y in range(l - 1):

        lowExamScore = 999
        lowIndex = y

        for x in range(y, l):
            if ExamScore[x] < lowExamScore:
                lowExamScore = ExamScore[x]
                lowIndex = x

        # Swap scores
        ExamScore[y], ExamScore[lowIndex] = ExamScore[lowIndex], ExamScore[y]

        # Swap names
        lastName[y], lastName[lowIndex] = lastName[lowIndex], lastName[y]

lastName = ["Adams", "Barcenas", "Browere", "Carlson",
            "Edstrom", "Hsieh", "Jones", "Kim",
            "Lee", "Ling"]

ExamScore = [100, 89, 75, 90, 79, 77, 88, 99, 85, 95]

hilow(lastName, ExamScore)

displayExam(lastName, ExamScore)
rdisplay(lastName, ExamScore)