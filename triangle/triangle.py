#Chuong trinh nhan dien tam giac
import math;
def checkValue(a,b,c):
    if(a <= 0) or (a > (2**31-1)):
        return 0
    elif(b <= 0) or (b > (2**31-1)):
        return 0
    elif(c <= 0) or (c > (2**31-1)):
        return 0
    else:
        return 1

#Kiem tra co kha nang tro thanh tam giac khong
def checkTriange(a,b,c):
    if ((a + b) > c) and ((a + c) > b) and ((c + b) > a):
        return 1
    else:
        return 0
    
#Kiem tra xem co phai tam giac vuong khong
def checkRightTriangle(a,b,c):
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (c**2 + b**2 == a**2):
        return 1
    else:
        return 0
        

#Kiem tra xem co phai tam giac can khong
def checkIsoscelesTriangle(a,b,c):
    if ((a == b and a != c) or (a == c and a != b) or (c == b and c != a)):
        return 1
    else:
        return 0

#Kiem tra xem co phai tam giac deu khong
def checkEquilateralTriangle(a,b,c):
    if a == b == c:
        return 1
    else:
        return 0

#Kiem tra xem co phai tam giac vuong can khong
def checkRightIsocelesTriangle(a,b,c):
    if checkRightTriangle(a, b, c) and checkIsoscelesTriangle(a, b, c):
        return 1
    else:
        return 0

def detect_triangle(a,b,c):
    
    if checkValue(a, b, c):
        if checkTriange(a, b, c):
            #La tam giac deu
            if checkEquilateralTriangle(a, b, c):
                return 1
            #La tam giac vuong can
            elif checkRightIsocelesTriangle(a, b, c):
                return 2
            #La tam giac can
            elif checkIsoscelesTriangle(a, b, c):
                return 3
            #La tam giac vuong
            elif checkRightTriangle(a, b, c):
                return 4
            else:
                #La tam giac thuong
                return 5
        else:
            return 0
    else:
        return -1
    