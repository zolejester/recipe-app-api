from django.test import SimpleTestCase

from app import cal


class CalTests(SimpleTestCase):

    def test_add_numbers(self):

        res = cal.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = cal.subtract(10, 15)
        self.assertEqual(res, -5)
