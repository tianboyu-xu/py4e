try:
    Hours = float(input('Enter Hours:'))
    Rate = float(input('Enter Rate:'))
    print('Pay=', Hours*Rate)
except:
    print('Please enter number only')
