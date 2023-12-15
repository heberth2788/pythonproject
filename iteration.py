""" 
Comment 
of 
multiple 
lines 
"""
# Comment of one line

# for statement
listA = [1, 2, 3, 4, 5]
print("Start the bucle 'for'")
for aux in listA:
    print("Aux =", aux) # print("Aux = " + str(aux))
else:
    print("'else' sentence and end of bucle 'for'")
print("End of 'for' and 'else' sentences\n")

# while statement
num = 0
while num <= 5:
    print(num, "HD") # print(str(num) + "HD")
    num += 1
else:
    print("'eslse' sentence and end of bucle 'while'\n")

# break statement
num = 0
while num <= 100:
    print(num, "HD") # print(str(num) + "HD")
    num += 1
    if num == 10:
        break # break doesn't allow that else execution
else:
    print("Else of while\n")

for aux in listA:
    print("Aux =", aux)
    if aux == 3:
        break # break doesn't allow that else execution
else:
    print("Else of for\n")
print("Kernel panic\n")

# continue statement
num = 0
while num <= 100:
    num += 1
    if num > 10:
        continue
    print(num, "HD") # print(str(num) + "HD")
else:
    print("Else of while\n")

for aux in listA:
    if aux > 3:
        continue
    print("Aux =", aux)
else:
    print("Else of for\n")

# pass statement: null operation
for aux in listA:
    print(aux)
    pass
    print(aux)
else:
    print("Else of for\n")

