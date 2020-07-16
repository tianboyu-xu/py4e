maxfind = None
minfind = None

while True:
    line = input('Enter a number:')
    if line == 'done':
        break
    try:
        itervar = float(line)
        if maxfind is None:
            maxfind = itervar
        elif itervar > maxfind:
            maxfind = itervar
        if minfind is None:
            minfind = itervar
        elif itervar < minfind:
            minfind = itervar
    except:
        print('Bad data')
        continue

print('min=', minfind, 'max=', maxfind)
