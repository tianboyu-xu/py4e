try:
    Score = float(input('Enter score:'))
except:
    print('Bad Score')

def computegrade(score):
    if score >= 0 and score <= 1:
        if score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7:
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        elif score < 0.6:
            grade = 'F'
    else:
        grade = 'Please enter grade from 0 to 1'
    return grade

try:
    final = computegrade(Score)
    print(final)
except:
    None
