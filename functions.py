def test_function():
    """
    Comment
    of
    multiple
    lines
    """
    pass
test_function()

#def sum(a, b):
#def sum(a, b) -> int:
def sum(a: int, b: int) -> int:
    """
    Comment
    of
    multiple
    lines
    """
    return a + b
s1: int = sum(5, 6)
print(s1)

# Defining a constant
PI = 3.1416
print(PI)

# Function with default arguments
def sum_default(a: int = 100, b: int = 100) -> int:
    return a + b
s2: int = sum_default(a = 5, b = 6) # 11
s2 = sum_default(5, 6) 
print(s2) # 11
s2 = sum_default() 
print(s2) # 200
s2 = sum_default(b = 5)
print(s2) # 105
s2 = sum_default(a = 6) # 106
print(s2)

def say_hello(name: str = "world"):
    print(f"Hello {name} !")
say_hello()
say_hello("HD")

# x: str = input("Say your name: ")
# say_hello(x)

"""
Package functions of Python
"""
aux = abs(-255)
print(f"{aux} = {type(aux)}")

aux = all(c.isupper() for c in "HELLO")
print(f"{aux} = {type(aux)}")


