# coding=UTF-8
import unittest


class ProfitCalc(object):
    def __init__(self):
        self.content = {}
    
    def add(self, code, qty, price):
        if code in self.content.keys():
            sum_price = self.content[code]['PRICE'] * self.content[code]['QTY'] + price
            self.content[code]['QTY'] += qty
            self.content[code]['PRICE'] = sum_price / self.content[code]['QTY']
        else:
            self.content[code] = {'QTY': qty, 'PRICE': price}
    
    def summary(self):
        return self.content


class ProfitTestCase(unittest.TestCase):
    def test_收到成交回報的紀錄商品_口數_價格能累計(self):
        sut = ProfitCalc()
        sut.add('TXO', 1, 9000)
        sut.add('TXO', 1, 9002)
        expect = {"TXO": {'QTY': 2, 'PRICE': (9000 + 9002) / 2}}
        actual = sut.summary()
        self.assertDictEqual(expect, actual)
        
        if __name__ == '__main__':
            unittest.main()


