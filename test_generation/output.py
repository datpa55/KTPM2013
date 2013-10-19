#Cac thu vien duoc import o day
import re
import unittest
from input import main

#Tach doan cmt khoang cua cac bien, bo di tat ca cac dau cach
def get_command(fname):
    cmt = []
    cout = 0
    number_line = 0
    with open(fname) as file:
        for line in file:
            if "'''" in line and cout==0:
                cout = 1
                continue       
            if "'''" in line and cout==1:
                cout = 0
                continue
            if cout==1:
                number_line += 1
                line = line.split(' ')
                A = ''.join(line)
                cmt.append(A)
    return cmt

#Lay ra khoang gia tri cua moi bien tuong ung
def get_values(arr, size):
    arr = map(int, re.findall(r'\d+', arr))
    chunks  = [ arr[start:start+size] for start in range(0, len(arr), size)]
    return chunks
    
#Kiem tra xem khoang gia tri co hop le hay khong, neu hop le tra ve thu tu sap xep cac khoang
def check_values(arr):
    for x in arr:
        if x[0] < x[1]:
            for y in arr:
                if y != x:
                    if ( y[0] > x[0] and y[0] < x[1] ) or ( y[1] > x[0] and y[1] < x[1] ):
                        return -1
                        break
        else:
            return -1
    return arr
    
#Lay o moi khoang da xac dinh tren mot gia tri dai dien cho khoang.
def get_testValue(arr):
    value = []
    for a in arr:
        value.append(a[0])
    return value
    
#Tich de cac cua cac bo
def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
        
    
#Ham chinh cua thu vien
def run_get_value(fname):
    cmd = get_command(fname);
    value = []
    for i in cmd:
        i = get_values(i, 2)
        if check_values(i) != -1:
            value.append(check_values(i))
        else:
            value = []
            break
    testValue = []
    if value != []:
        for a in value:
            testValue.append(get_testValue(a))
    return testValue
    
class Test(unittest.TestCase):
    pass
    
def test_generation(arr):
    def test(self):
        self.assertEqual(main(*arr), 'x')
    return test
        
if __name__ == "__main__":
    
    arr = []
    arr = run_get_value("input.py")
    if arr == []:
        raise Exception("wrong input")
    else:
        test_arr = []
        for x in product(*arr):
            test_arr.append(x)
        for x in test_arr:
            test_name = 'test_%s' % test_arr.index(x)
            test = test_generation(x)
            setattr(Test, test_name, test)
        unittest.main()