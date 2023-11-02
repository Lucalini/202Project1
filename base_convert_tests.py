import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2_1(self):
        self.assertEqual(convert(45,2),"101101")
    def test_base2_2(self):
        self.assertEqual(convert(0,2),"0")
    def test_base2_3(self):
        self.assertEqual(convert(999999987654321,2),"11100011010111111010100100000010100001111010110001")

    def test_base3(self):
        self.assertEqual(convert(568,3 ),"210001")

    def test_base4_1(self):
        self.assertEqual(convert(30,4),"132")
    def test_base4_2(self):
        self.assertEqual(convert(30,4),"132")
    def test_base5(self):
        self.assertEqual(convert(214, 5),"1324")
    def test_base6(self):
        self.assertEqual(convert(100,6),"244")
    def test_base7(self):
        self.assertEqual(convert(82, 7),"145")

    def test_base8(self):
        self.assertEqual(convert(247, 8),"367")

    def test_base9(self):
        self.assertEqual(convert(103, 9),"124")
    def test_base10(self):
        self.assertEqual(convert(10, 10),"10")
    def test_base10_2(self):
        self.assertEqual(convert(19230, 10),"19230")

    def test_base11(self):
        self.assertEqual(convert(164, 11),"13A")
    def test_base12(self):
        self.assertEqual(convert(135,12),"B3")
    def test_base13(self):
        self.assertEqual(convert(161, 13),"C5")
    def test_base14(self):
        self.assertEqual(convert(200,14),"104")
    def test_base15(self):
        self.assertEqual(convert(912, 15),"40C")

    def test_base16_1(self):
        self.assertEqual(convert(316,16),"13C")
    def test_base16_2(self):
        self.assertEqual(convert(29394,16),"72D2")



if __name__ == "__main__":
        unittest.main()
