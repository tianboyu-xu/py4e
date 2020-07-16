try:
    Hours = float(input('Enter Hours:'))
    Rate = float(input('Enter Rate:'))
    if Hours >=0 and Rate >= 0 :
        if Hours <= 40 :
            print('Pay=', Hours*Rate)
        elif Hours > 40:
            print('Pay=', Hours*Rate*1.5)
    else :
        print('Please enter a positive number')
except:
    print('Error, please enter numeric input')


