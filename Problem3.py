class Grade:
    def __init__(self,Input):
        self.Input = Input

    def getGrade(self):
        AverageGrade = sum(self.Input) / len(self.Input)
        print(f"Average Grade: {AverageGrade:.2f}")
        PointGrade = ((100 - AverageGrade)+10)/10
        print(f"Point Grade:{PointGrade:.2f}")
        if AverageGrade < 50:
            print("Dropped")
        elif AverageGrade  < 75:
            print("Failed")
        elif AverageGrade  < 79:
            print("Passed -> Satisfactory")
        elif AverageGrade < 84:
            print("Passed -> Good")
        elif AverageGrade < 89:
            print("Passed: Average")
        elif AverageGrade < 99:
            print("Passed -> Very Good")
        elif AverageGrade == 100:
            print("Passed -> Excellent")

grades = []

while True:
    grade = float(input("Enter your grade (Enter -1 to end): "))
    if grade == -1:
        break
    elif 0 <= grade <= 100:
        grades.append(grade)
    else:
        print("Invalid Input. Try again")

    a = Grade(grades)
a.getGrade()
