import unittest
from triangle import detect_triangle
import math

class Test(unittest.TestCase):
    #Test gia tri dau vao
    def testNumber1(self):
        self.assertEqual(detect_triangle(3, -5, 7) , -1)
        self.assertEqual(detect_triangle(-3.4, 2, 1), -1)
        self.assertEqual(detect_triangle(7, 2.7, -1.6), -1)
    
    
    def testNumber2(self):
        self.assertEqual(detect_triangle("dat", 3, 6), -1)
        self.assertEqual(detect_triangle(3.2, "a", 9), -1)
        self.assertEqual(detect_triangle(4.6 , 6 , "a"), -1)
        
    def testNumber3(self):
        self.assertEqual(detect_triangle(2, 5, 2**31), -1)
        self.assertEqual(detect_triangle(2**31, 5, 2), -1)
        self.assertEqual(detect_triangle(5, 2**31, 2), -1)
        
    def testNumber4(self):
        self.assertEqual(detect_triangle(7, 0, 2), -1)
        self.assertEqual(detect_triangle(0, 7, 2), -1)
        self.assertEqual(detect_triangle(7, 2, 0), -1)
        
    #Test truong hop co phai tam giac hay khong
    def testNumber5(self):
        self.assertEqual(detect_triangle(1, 2, 4), 0)
        self.assertEqual(detect_triangle(1.3, 3.2, 4.7), 0)
        self.assertEqual(detect_triangle(math.sqrt(3), 2, 7), 0)
    
    #test truong hop la tam giac thuong
    def testNumber6(self):
        self.assertEqual(detect_triangle(3, 5, 7), 5)
        self.assertEqual(detect_triangle(1, 5.3, 7), 5)
        self.assertEqual(detect_triangle(math.sqrt(5), 5, 7), 5)
    
    #Test truong hop la tam giac deu
    def testNumber7(self):
        self.assertEqual(detect_triangle(6, 6, 6), 1)
        self.assertEqual(detect_triangle(4.2, 4.2, 4.2), 1)
        self.assertEqual(detect_triangle(math.sqrt(7), math.sqrt(7), math.sqrt(7)), 1)
        
    def testNumber8(self):
        self.assertEqual(detect_triangle(0.00002, 0.00002, 0.0002), 2)
        
    #Test truong hop la tam giac vuong can
    def testNumber9(self):
        self.assertEqual(detect_triangle(2 , 2, 2*math.sqrt(2)), 2)
        
    #Test truong hop la tam giac can
    def testNumber10(self):
        self.assertEqual(detect_triangle(4, 4, 2), 3)
    
    #Test truong hop la tam giac vuong
    def testNumber11(self):
        self.assertEqual(detect_triangle(3, 4, 5), 4)
        
    
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()