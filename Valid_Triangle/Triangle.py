a = int(input("Enter a : - "))
b = int(input("Enter b : - "))
c = int(input("Enter c : - "))


def valid_triangle(a , b , c):

    # Check whether all sides are positive
    if a > 0 and b > 0 and c > 0:
    
        # Check Triangle Inequality Theorem
        if (a+b)>c and (a+c)>b and (b+c)>a:
            # All three side are equal
            if a==b == c:
                return "Valid Traingle and Equilateral "
            
            # Any two side are equal
            elif a == b or b==c or c==a:
                return "Isosceles Triangle "
            
            # All three side are different
            elif a != b and b!=c :
                return "Scalen Triangle "
        return "Not valid triangle "
    return "Not valid triangle "

print(valid_triangle(a , b ,c ))
            