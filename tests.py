#Шестиричный калькулятор

import unittest
from main import Ui_MainWindow


class SumTestCase(unittest.TestCase):

    def to_six(self, numder: int) -> str:
        answer = ''
        if numder == 0:
            return '0'
        if numder > 0:
            while numder > 0:
                answer = str(numder % 6) + answer
                numder //= 6
            return answer
        else:
            numder = abs(numder)
            while numder > 0:
                answer = str(numder % 6) + answer
                numder //= 6
            return '-' + answer

    def test_sum(self):
        a = '21'
        b = '5'
        op: str = '+'
        answer = Ui_MainWindow.calculation(self, a, b, op)
        self.assertEqual(answer, '30')

    def test_sub(self):
        a = '21'
        b = '5'
        op: str = '-'
        answer = Ui_MainWindow.calculation(self, a, b, op)
        self.assertEqual(answer, '12')

    def test_sub_minus(self):
        a = '-21'
        b = '5'
        op: str = '+'
        answer = Ui_MainWindow.calculation(self, a, b, op)
        self.assertEqual(answer, '-12')

    def test_to_six_plus(self):
        num = 72
        answer = Ui_MainWindow.to_six(self, num)
        self.assertEqual(answer, '200')

    def test_to_six_minus(self):
        num = -72
        answer = Ui_MainWindow.to_six(self, num)
        self.assertEqual(answer, '-200')

    def test_to_six_zero(self):
        num = 0
        answer = Ui_MainWindow.to_six(self, num)
        self.assertEqual(answer, '0')



