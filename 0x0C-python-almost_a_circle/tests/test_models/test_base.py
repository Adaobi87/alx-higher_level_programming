import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_constructor_with_id(self):
        b = Base(id=1)
        self.assertEqual(b.id, 1)
    
    def test_constructor_without_id(self):
        b1 = base()
        b2 = base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

if __name__ == "__main__":
    unittest.main()
