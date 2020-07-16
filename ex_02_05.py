try:
    temp_C =float(input('Please enter temperature in Celsius:'))
    temp_F = temp_C*1.8+32
    print('The temperature in', temp_C , 'Celsius is equal to', temp_F , 'in Fahrenheit')
except:
    print('Please enter number only.')
