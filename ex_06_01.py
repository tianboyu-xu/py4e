str = 'X-DSPAM-Confidence:0.8475'
line = str.find(':')
end = str[line+1:]
final = float(end)
print(final)
