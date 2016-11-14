# coding=UTF-8
import unittest


class ProfitCalc(object):
    def __init__(self):
        self.content = {}
    
    def add(self, code, qty, price):
        item = {'QTY': qty, 'PRICE': price}
        if code in self.content.keys():
            sum_price = self.content[code]['PRICE'] * self.content[code]['QTY']
            item['QTY'] = self.content[code]['QTY'] + qty
            if item['QTY'] == 0:
                del self.content[code]
                return
            else:
                item['PRICE'] = (sum_price + price * qty) / item['QTY']
        self.content[code] = item
    
    def summary(self):
        return self.content
    
    def calc_profit(self, code, quote):
        profit = 0
        if code in self.content.keys():
            item = self.content[code]
            profit = (quote - item['PRICE']) * item['QTY'] * 200
        
        return profit


class ProfitTestCase(unittest.TestCase):
    def test_收到成交回報的紀錄商品_口數_價格能累計(self):
        sut = ProfitCalc()
        sut.add('TXO', 1, 9000)
        sut.add('TXO', 1, 9002)
        expected = {"TXO": {'QTY': 2, 'PRICE': (9000 + 9002) / 2}}
        actual = sut.summary()
        self.assertDictEqual(expected, actual)
    
    def test_收到成交回報的紀錄商品_口數_價格剛好沒有部位(self):
        sut = ProfitCalc()
        sut.add('TXO', 1, 9000)
        sut.add('TXO', 1, 9002)
        sut.add('TXO', -2, 9000)
        expected = {}
        actual = sut.summary()
        self.assertDictEqual(expected, actual)
    
    def test_報價變動_能顯示損益變化(self):
        sut = ProfitCalc()
        sut.add('TXO', 1, 9000)
        sut.add('TXO', 1, 9000)
        actual = sut.calc_profit('TXO', 9010)
        expected = (9010 - 9000) * 2 * 200  # (Quote - AvgPrice) * QTY * 200
        self.assertEqual(expected, actual)
    
    if __name__ == '__main__':
        unittest.main()
