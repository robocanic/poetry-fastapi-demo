from poetry_demo.module1.calc import square, subtract, cube, add


class TestCalc:

    def test_square(self):
        assert square(3) == 9

    def test_subtract(self):
        assert subtract(6, 3) == 9

    def test_cube(self):
        assert cube(3) == 27

    def test_add(self):
        assert add(3, 6) == 9
