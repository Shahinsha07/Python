import unittest


def add(a,b):
    return a+b


class unitytesting(unittest.TestCase):
    # def test1(self):
    #     self.assertEqual(add(2,3),5)
    # def test2(Self):
    #     self.assertTrue("ABC".isupper())

    # def test3(self):
    #     self.assertFalse("ABC".isupper())
    # def test4(self):
    #     result=10
    #     self.assertGreater(result,5)
    
    # def test5(self):
    #     result=[1,2,3,4,5]
    #     self.assertIn(5,result)
    
    # def test7(self):
    #     result=[1,2,3,4,5]
    #     self.assertIn(result,5)

    # def test6(self):
    #     self.assertNotEqual(add(1,2),4)

    # def test8(self):
    #     self.assertFalse('HAi'.isupper())
    
    # def test9(self):
    #     result=[1,2,3,4,5]
    #     self.assertNotIn(51,result)

    # def test10(self):
    #     l1=[1,2,3]
    #     l2=[1,2,3]
    #     self.assertListEqual(l1,l2)

    # def test11(self):
    #     l1=(1,2,3)
    #     l2=(1,2,3)
    #     self.assertTupleEqual(l1,l2)

    # def test11(self):
    #     d1={"a":1,"b":2,"c":3}
    #     d2={"a":1,"b":2,"c":3}
    #     self.assertDictEqual(d1,d2)

    # def test12(self):
    #     self.assertCountEqual([1,2,3],[1,2,3])

    # def test13(self):
    #     self.assertCountEqual([1,2,3],[2,3,1])

    # def test14(self):
    #     self.assertCountEqual([1,2,3],[4,3,1])

    # def test15(self):
    #     self.assertRegex("hello","^h.*$")
    # def test16(self):
    #     self.assertNotRegex("hello","^x.*$")

    # def test17(self):
    #     result=5
        # self.assertGreaterEqual(result,5)

    # def test18(self):
    #     result=3
    #     self.assertLess(result,5)

    def test19(self):
        result=5
        self.assertLessEqual(result,10)


    

if __name__=="__main__":
    unittest.main()