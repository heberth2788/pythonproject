# Tuplas are inmutables
tuplaA = (1, 2, 3, 4, 5, 6, False, "Heberth", 3.5, 'C')
print(tuplaA)
print(tuplaA[-2])
print(2 in tuplaA)
print(tuplaA[0:7])

tuplaB = (True, False, "HD")
tuplaC = tuplaA + tuplaB
print(tuplaC)
print(tuplaA == tuplaC)
print(tuplaB * 3)





