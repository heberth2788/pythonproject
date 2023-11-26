# f-strings : for String interpolation with {<variableName>}
pivot = 27
print(f'Hello Python world - {pivot} !')

# Comments: 
''' Multi line comment
with
python
'''
# Another comment

# Integer, Float, String, Boolean, List, Dictionary, Tuple, Set
year = 1988; # Int
pi = 3.1416; # Float
name = 'Heberth '; # String
fullName = name + 'Deza' # String
isMale = True;

print(f'My name is {fullName}.')
# input()

# Implicit convertion: int(), float(), str(), bin(), oct(), hex()
yearStr = "1988"
yearInt = int(yearStr)
print(f'yearStr = {yearStr} , yearInt = {yearInt}')

yearStrAux = str(yearInt)
print(f'Int to String = {yearStrAux}')

print(f'Int to bin = {bin(yearInt)} , to oct = {oct(yearInt)} , to hex = {hex(yearInt)}')

# Operators: +, -, *, %, / (division), ** (exponentiation), // (Integer division)

ten = 10
three = 3
print(f'Operators with number {ten} and {three} : \n + : {ten + three} , - : {ten - three} , * : {ten * three} , / : {ten / three} , % : {ten % three} , ** : {ten ** three} , // : {ten // three}')

# Operator +(Concat) and *(Repeat) in String
print('Hi ' * 5)
print('Hi' + ' ' + 'Heberth')
strAux = 'Heberth Deza'

# Character and ranges in String
print(strAux[2])
print(strAux[2:7])

# Asking for a character in a String
print('b' in strAux)
print('b' not in strAux)

# Comparing: ==, !=, <, >, <=, >=
print(f'< : {ten < three}')
print(f'> : {ten > three}')
print(f'== : {ten == 10}')

# Boolean operators: not, and, or
trueAux = True
falseAux = False
print(not trueAux)
print(trueAux and falseAux)
print(trueAux or falseAux)

# Conditionals: if, elif, else
size = 1.70
maxSize = 1.70

if(size < maxSize) :
    print('Rejected')
    print('R1')
    print('R2')
elif(size == maxSize and trueAux) :
    print('Accepted by equal')
    print('AE1')
    print('AE2')
else :
    print('Accepted')
    print('A1')
    print('A2')
print('End of conditionals')

# Ternary operator: 'if else' , Format: 'val1' if 'condition' else 'val2'
val1 = 5
val2 = 6
pivotA = val1 if val1 > val2 else val2
print(f'{pivotA}')

