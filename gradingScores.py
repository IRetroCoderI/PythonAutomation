
def calculate_grade(scores):
    if not scores:
        return None
    
    average = sum(scores)/len(scores)
    print(average)
    if average >= 99:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    
studentScores = [20, 30, 80, 100, 100, 20, 30, 40, 60]

grade = calculate_grade(studentScores)
print(f"The student's grade is {grade}")