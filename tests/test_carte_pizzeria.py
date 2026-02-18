import unittest
from unittest.mock import Mock 
from src import CartePizzeria
from src import Pizza

class TestCartePizzeria(unittest.TestCase):

    def setUp(self):
        """Initialisation avant chaque test."""
        self.carte = CartePizzeria()
    
    def test_add_pizza(self): 
        
        pizza_mock = Mock()
        
        self.carte.add_pizza(pizza_mock)
        
        assert self.carte.nb_pizzas() == 1
        assert self.carte.is_empty() is False

    def test_is_empty(self):
        assert self.carte.is_empty() is True
        
        pizza_mock = Mock()
        self.carte.add_pizza(pizza_mock)
        assert self.carte.is_empty() is False

    def test_nb_pizzas(self):
        assert self.carte.nb_pizzas() == 0
        
        p1 = Mock()
        p2 = Mock()
        self.carte.add_pizza(p1)
        self.carte.add_pizza(p2)
        assert self.carte.nb_pizzas() == 2

    def test_remove_pizza(self):
        pizza_mock = Mock()
        pizza_mock.nom = "Margherita" 
        self.carte.add_pizza(pizza_mock)
        assert self.carte.nb_pizzas() == 1
        
        self.carte.remove_pizza("Margherita")
        
        assert self.carte.nb_pizzas() == 0
        assert self.carte.is_empty() is True

if __name__ == '__main__':
    unittest.main()