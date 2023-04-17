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

    def test_y_string(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 10, 20)

    def test_area(self):
        self.assertEqual(self.r.area(), 5 * 10)
        rect = Rectangle(3, 9, 8, 8, 2)
        self.assertEqual(rect.area(), 3 * 9)

    def test_str_overload(self):
        r = Rectangle(5, 10, 8, 7, 88)
        self.assertEqual(r.__str__(), "[Rectangle] (88) 8/7 - 5/10")

    def test_update_id(self):
        self.r.update(54)
        self.assertEqual(54, self.r.id)

    def test_update_width(self):
        self.r.update(54, 30)
        self.assertEqual(30, self.r.width)

    def test_update_height(self):
        self.r.update(54, 30, 10)
        self.assertEqual(10, self.r.height)

    def test_update_x(self):
        self.r.update(54, 30, 10, 6)
        self.assertEqual(6, self.r.x)

    def test_update_y(self):
        self.r.update(54, 30, 10, 6, 2)
        self.assertEqual(2, self.r.y)

    def test_update_dict(self):
        self.r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(1, self.r.y)
        self.assertEqual(2, self.r.width)
        self.assertEqual(3, self.r.x)
        self.assertEqual(89, self.r.id)

    def test_update_dict_list(self):
        self.r.update(1000, y=1, width=2, x=3, id=89)
        self.assertEqual(1000, self.r.id)

    def test_to_dict(self):
        r1 = Rectangle(5, 4)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_saving_to_file(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        r1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file([r1])

        with open("Rectangle.json", "r") as file:
            content = file.read()
        t = [{"x": 0, "y": 0, "id": 346, "height": 10, "width": 5}]
        self.assertEqual(t, json.loads(content))

    def test_json_string(self):
            list_input = [
                {'id': 2089, 'width': 10, 'height': 4},
                {'id': 2712, 'width': 1, 'height': 7}]
            json_list_input = Rectangle.to_json_string(list_input)
            list_output = Rectangle.from_json_string(json_list_input)
            s1 = {'id': 2089, 'width': 10, 'height': 4}
            s2 = {'height': 7, 'id': 2712, 'width': 1}
            self.assertEqual(list_input[0], s1)
            self.assertEqual(list_input[1], s2)


if __name__ == "__main__":
    unittest.main()
