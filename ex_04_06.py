try:
    Hours = float(input('Enter Hours:'))
    Rate = float(input('Enter Rate:'))
except:
    print('Error, please enter numeric input')

def computepay(hours,rate):
    if hours >=0 and rate >= 0 :
        if hours <= 40 :
                pay= hours*rate
        elif Hours > 40:
                pay= hours*rate*1.5
    else :
            print('Please enter a positive number')
    return pay

try:
    Pay = computepay(Hours,Rate)
    print('Pay:', Pay)
except:
    None
