# coding=UTF-8
import unittest


class ProfitTestCase(unittest.TestCase):
    def test_收到成交回報的紀錄商品_口數_價格能累計(self):
        sut = ProfitCalc()
        sut.Add('TXO', '1', '9000')
        sut.Add('TXO', '1', '9002')
        
        
        


if __name__ == '__main__':
    unittest.main()
