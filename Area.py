import math
print("1 : Equilateral\n2 : Right angled\n3 : Isoscles")
a = int(input("Enter the number for respective triangle: "))

dict = {1: "Equilateral",
        2: "Right angled",
        3: "Isoscles"}


def Equilateral():
    s = float(input("The side of triangle: "))
    area = (math.sqrt(3)* s*s)/4
    print("area is", round(area,3))

def other():
    h = float(input("The height of triangle: "))
    b = float(input("The base of triangle: "))
    area = 0.5 * b
    print("area is", round(area,3))
    
def call(a):
    if a ==1:
        Equilateral()
    else:
        other()


if a in dict:
    print("Ok so the triangle is ", dict.get(a), call(a))
