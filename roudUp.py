a=input('Number to RoundUp:   ')
print  str((int(str(a).split('.')[1])/10.0+.5)+int(str(a).split('.')[0])).split('.')[0]
