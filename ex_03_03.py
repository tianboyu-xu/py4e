try :
    score = float(input('Enter score:'))
    if score >= 0 and score <= 1:
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        elif score < 0.6:
            print('F')
    else:
        print('Please enter grade from 0 to 1')
except :
    print('Bad Score')
