import matplotlib
count = 0
total = 0
while True:
    line = input('Enter a number:')
    if line == 'done':
        break
    try:
        itervar = float(line)
        total = total + itervar
        count = count + 1
    except:
        print('Bad data')
        continue

print('total=', total, 'count=', count, 'average=', total / count)
