side = []
for i in range(0,3):
    i = float(input("Enter the sides of triangle: "))
    side.append(i)
    
print("The perimeter of the triangle is", round(sum(side),3))