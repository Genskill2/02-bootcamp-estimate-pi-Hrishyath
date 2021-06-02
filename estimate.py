import math
import unittest
import random 

def wallis(i):
    pi=1   
    for x in range(1,i):
        pi=pi*(4*(x**2))/(4*(x**2)-1) 
    return 2*pi
    
def monte_carlo(i):
    C_area=0
    T_area=0
    prob=0
    for j in range(0,i):
        a=random.random()
        b=random.random()  
        D=(a**2+b**2)**0.5
        if D<=1:
            C_area+=1
            T_area+=1
            prob=4*C_area/T_area
        else:
            T_area+=1
            prob=4*C_area/T_area
    return prob

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
