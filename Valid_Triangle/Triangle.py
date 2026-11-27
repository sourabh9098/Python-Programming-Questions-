a = int(input("Enter a : - "))
b = int(input("Enter b : - "))
c = int(input("Enter c : - "))


def valid_triangle(a , b , c):

    if (a+b)>c and (a+c)>b and (b+c)>a:
        if a==b == c:
            return "Valid Traingle and Equilateral "
        elif a == b or b==c or c==a:
            return "Isosceles Triangle "
        elif a != b and b!=c :
            return "Scalen Triangle "
        
    return "Not valid triangle "

print(valid_triangle(a , b ,c ))
            