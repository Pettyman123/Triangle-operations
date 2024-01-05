a = []
x = int(input("enter the 1st angle: "))
y = int(input("enter the 2nd angle: "))
a.append(x)
a.append(y)

while sum(a) <=180:
    c = 180- x-y
    print("the 3rd angle is ",c)
    break