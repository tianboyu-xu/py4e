numlist = []
while True:
    num = input('Enter a number:')
    if num == 'done':
        break
    try:
        num = float(num)
        numlist.append(num)
    except:
        print('Please enter number only')
print('Maximum:', max(numlist))
print('Minimum:', min(numlist))
