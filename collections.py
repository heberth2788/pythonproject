# Lists: we can use negative index(Starting from right to left), for example: -1, -2, .... E.g: listHd[-3]
listAux = ["Heberth", "Deza", 35, "M", True, 1.73]
listInt = [35, 36, 14, 7]
print(listInt)
name = "Heberth"
surname = "Deza"
yearsOld = 35
isMarried = False
listHd = [name, surname, yearsOld, isMarried]
print(f'{listHd} : {listHd[-3]} ,  {listHd[1]}')
print(len(listHd))
listHd[3] = True
print(listHd)

# Operation with lists
print(f'sum = {sum(listInt)} , min = {min(listInt)} , max = {max(listInt)}') # Sum all the values of the list

# Array, 1D, 2D, 3D
import array as arr
arrayA = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2])
print(arrayA)
arrayB = arr.array('i', listInt)
print(arrayB)
arrayA.append(-3)
print(len(arrayA))

matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(f'A value of the matriz = {matriz[1][3]}')

# Dictiorary
hd = {
    'name' : 'Heberth',
    'surname' : 'Deza',
    'size' : 1.73,
    'age' : 35,
    'sex' : 'M',    
    #'sex' : 'F',
    'address' : {
        'city' : 'Guadalupe',
        'number' : 147,
    }
}
print(f'\nhd = {hd} , name = {hd["name"]} , age = {hd["age"]} , sex = {hd["sex"]} , \naddress = {hd["address"]["city"]}')
print(f'hd keys = {hd.keys()}')
print(f'hd.address keys = {hd["address"].keys()}')


# Functions: 'def' keyword
def say_ello(name) :
    print(f'\nHello {name} ')
    print('world!')
say_hello('HD')






