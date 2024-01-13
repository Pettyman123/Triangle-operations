import math

dict = {1: "Equilateral",
        2: "Right angled",
        3: "Isoscles"}

print("1 : Equilateral\n2 : Right angled\n")

a = int(input("Enter the number for respective triangle: "))


def Equilateral():
    area = float(input("The area of the triangle: "))
    side = math.sqrt(4*area/math.sqrt(3))
    perimeter = 3*side 
    print("perimeter is", round(perimeter,3))

def rightangled():
    area = float(input("The area of triangle: "))
    s = float(input("Enter the height or base of triangle: "))
    side = 2 * area / s
    perimeter = math.sqrt(side*side + s*s) + side + s
    print("perimeter is", round(perimeter,3))
    
def call(a):
    if a ==1:
        Equilateral()
    elif a ==2:
        rightangled()

if a in dict:
    print("Ok so the triangle is ", dict.get(a), call(a))

