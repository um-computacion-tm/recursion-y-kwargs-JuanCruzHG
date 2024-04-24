import unittest

def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

class TestFibonacci(unittest.TestCase):

    def test_0(self):
        resultado = fibonacci_recursivo(0)
        self.assertEqual(resultado, 0)

    def test_1(self):
        resultado = fibonacci_recursivo(1)
        self.assertEqual(resultado, 1)

    def test_2(self):
        resultado = fibonacci_recursivo(2)
        self.assertEqual(resultado, 1)

    def test_5(self):
        resultado = fibonacci_recursivo(5)
        self.assertEqual(resultado, 5)

    def test_10(self):
        resultado = fibonacci_recursivo(10)
        self.assertEqual(resultado, 55)

    def test_13(self):
        resultado = fibonacci_recursivo(13)
        self.assertEqual(resultado, 233)

if __name__ == '__main__':
    unittest.main()