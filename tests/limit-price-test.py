import unittest
from macro import Macro
from trade import Trade
from corporation import Corporation



trade = Trade()


class PriceLimitTest(unittest.TestCase ):
        
    def test_price(self):
        self.assertEqual({'up': 30, 'down': -30}, trade.price_limit(0))
        
    def test_price_2(self):
        self.assertEqual({'up': 31, 'down': -29}, trade.price_limit(1))
    
    def test_price_3(self):
        self.assertEqual({'up': 129, 'down': 69}, trade.price_limit(99))
        
    def test_price_4(self):
        self.assertEqual({'up': 130, 'down': 70}, trade.price_limit(100))
    
    def test_price_5(self):
        self.assertEqual({'up': 249, 'down': 149}, trade.price_limit(199))

    def test_price_6(self):
        self.assertEqual({'up': 250, 'down': 150}, trade.price_limit(200))

    def test_price_7(self):
        self.assertEqual({'up': 579, 'down': 419}, trade.price_limit(499))

    def test_price_8(self):
        self.assertEqual({'up': 600, 'down': 400}, trade.price_limit(500))

    def test_price_9(self):
        self.assertEqual({'up': 799, 'down': 599}, trade.price_limit(699))

    def test_price_10(self):
        self.assertEqual({'up': 850, 'down': 550}, trade.price_limit(700))

    def test_price_11(self):
        self.assertEqual({'up': 799, 'down': 599}, trade.price_limit(999))

    def test_price_11(self):
        self.assertEqual({'up': 850, 'down': 550}, trade.price_limit(1000))

    def test_price_11(self):
        self.assertEqual({'up': 1149, 'down': 849}, trade.price_limit(1499))

    def test_price_11(self):
        self.assertEqual({'up': 1300, 'down': 700}, trade.price_limit(1500))

    def test_price_11(self):
        self.assertEqual({'up': 1799, 'down': 1199}, trade.price_limit(1999))

    def test_price_11(self):
        self.assertEqual({'up': 1900, 'down': 1100}, trade.price_limit(2000))

    def test_price_11(self):
        self.assertEqual({'up': 2399, 'down': 1599}, trade.price_limit(2999))

    def test_price_11(self):
        self.assertEqual({'up': 2500, 'down': 1500}, trade.price_limit(3000))

    def test_price_11(self):
        self.assertEqual({'up': 3499, 'down': 2499}, trade.price_limit(4999))

    def test_price_11(self):
        self.assertEqual({'up': 3700, 'down': 2300}, trade.price_limit(5000))

    def test_price_11(self):
        self.assertEqual({'up': 7999, 'down': 4299}, trade.price_limit(6999))

    def test_price_11(self):
        self.assertEqual({'up': 8500, 'down': 5500}, trade.price_limit(7000))

    def test_price_11(self):
        self.assertEqual({'up': 11499, 'down': 8499}, trade.price_limit(9999))

    def test_price_11(self):
        self.assertEqual({'up': 13000, 'down': 7000}, trade.price_limit(10000))

if __name__ == "__main__":
    unittest.main()