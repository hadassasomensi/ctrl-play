import unittest 

# def soma(a,b):
#     return a + b

# class testSoma(unittest.TestCase):

#     def testSomaPositivos(self):
#         self.assertEqual(soma(2,3), 5)

#     def testSomaNegativos(self):
#         self.assertEqual(soma(-2,-3), -5)

#     def testSomasZeros(self):
#         self.assertEqual(soma(0,0), 0)

# if __name__ == '__main__':
#     unittest.main()        


# def dividir(a,b):
#     if b == 0:
#        raise ValueError("divisao por 0 nao permitida")
#     else:
#         return a/b
# class testDividir(unittest.TestCase):
   
#    def testDivisaoPorZero(self):
#       with self.assertRaises(ValueError):dividir(10,6)

# if __name__ == '__main__':
#    unittest.main()



class calculadora:
    def __init__(self):
        self.resultado = 0

    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        if b == 0:
            raise ValueError("divisao por zero")
        else: 
            return a / b
        
class testCalculadora(unittest.TestCase):

    def setUp(self):
        self.C = calculadora()
    
    def testSoma(self):
        self.assertEqual(self.C.soma(5,6),11)

    def testSubtracao(self):
        self.assertEqual(self.C.subtracao(7,3),4)

    def testMultiplicacao(self):
        self.assertEqual(self.C.multiplicacao(2,3),6)

    def testDivisao(self):
        self.assertEqual(self.C.divisao(5,1),5)

    def testDivisaoPorZero(self):
        with self.assertRaises(ValueError): self.C.divisao(10,0)

if __name__ == '__main__':
    unittest.main()

