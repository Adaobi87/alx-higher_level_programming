import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_attributes(self):
        r1 = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r1.id, 50)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 30)
        self.assertEqual(r1.y, 40)

        r1.width = 100
        r1.height = 200
        r1.x = 300
        r1.y = 400

        self.assertEqual(r1.width, 100)
        self.assertEqual(r1.height, 200)
        self.assertEqual(r1.x, 300)
        self.assertEqual(r1.y, 400)

    def test_constructor_without_id(self):
        r1 = Rectangle(10, 20, 30, 40)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 30)
        self.assertEqual(r1.y, 40)

        r2 = Rectangle(100, 200, 300, 400)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 100)
        self.assertEqual(r2.height, 200)
        self.assertEqual(r2.x, 300)
        self.assertEqual(r2.y, 400)

    def test_constructor_with_id(self):
        r1 = Rectangle(10, 20, 30, 40, 50)
        self.assertEqual(r1.id, 50)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 30)
        self.assertEqual(r1.y, 40)

        r2 = Rectangle(100, 200, 300, 400, 500)
        self.assertEqual(r2.id, 500)
        self.assertEqual(r2.width, 100)
        self.assertEqual(r2.height, 200)
        self.assertEqual(r2.x, 300)
        self.assertEqual(r2.y, 400)
    
    def test_width_string(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 10)

    def test_width_bool(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(True, 10)

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-9, 10)

    def test_height_string(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "10")

    def test_height_bool(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(True, 10)

    def test_height_negative(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-9, 10)

    def test_x_string(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 10, 32)

    def test_

if __name__ == "__main__":
    unittest.main()
