a = int(input('Type een getal in'))
b = 5

if a >= b:
    print('Je kunt een groot zak patat kopen.')
elif a >= 3:
    min = a
    print('Je kunt een middel zak patat kopen. '+ str(min))
else:
    print('Je hebt niet genoeg geld om een zak patat te kopen.')
