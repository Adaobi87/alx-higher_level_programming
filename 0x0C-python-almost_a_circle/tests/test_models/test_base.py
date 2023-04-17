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

    def test_id_zero(self):
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        b = Base(-5)
        self.assertEqual(-5, b.id)

    def test_id_string(self):
        b = Base("John")
        self.assertEqual("John", b.id)

    def test_id_list(self):
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        b = Base({"id": 99})
        self.assertEqual({"id": 99}, b.id)

    def test_id_tuple(self):
        b = Base((8,))
        self.assertEqual((8,), b.id)

    def test_to_json_type(self):
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

if __name__ == "__main__":
    unittest.main()
