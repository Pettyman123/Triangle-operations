import math

dict = {1: "Equilateral",
        2: "Right angled",
        3: "Isoscles"}

print("1 : Equilateral\n2 : Right angled\n3 : Isoscles")

a = int(input("Enter the number for respective triangle: "))


def Equilateral():
    area = float(input("The area of the triangle: "))
    side = math.sqrt(4*area/math.sqrt(3)) 
    print("side is", round(side,3))

def other():
    area = float(input("The area of triangle: "))
    s = float(input("Enter the height or base of triangle: "))
    side = 2 * area / s
    print("side is", round(side,3))
    
def call(a):
    if a ==1:
        Equilateral()
    else:
        other()

if a in dict:
    print("Ok so the triangle is ", dict.get(a), call(a))

