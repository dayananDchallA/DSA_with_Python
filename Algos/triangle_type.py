def traingle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b and a == c and b == c:
            print("Equilateral Triangle")
        elif a == b or a == c or b == c:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
    else:
        print("Not a Triangle")

traingle_type(1, 2, 3)
traingle_type(3, 4, 5)