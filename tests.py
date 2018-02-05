from unittest import TestCase

from find_array import find_array


class FindArrayTestCase(TestCase):
    def setUp(self):
        self.array = range(20, 30) + range(10, 30, 2) + range(1, 15)
        self.sub = [1, 3, 4]

    def test_not_exist(self):
        self.assertFalse(find_array(self.sub, self.array))

    def test_exist(self):
        self.assertTrue(find_array([21, 22], self.array))

    def test_found(self):
        self.array += self.sub
        print self.array
        self.assertTrue(find_array(self.sub, self.array))

    def test_no_iteration(self):
        self.assertFalse(find_array(self.sub, [1,2,3,4]))

    def test_the_same(self):
        self.assertTrue(find_array(self.sub, self.sub))

    def test_bug(self):
        self.assertTrue(find_array(self.sub, [1,1,3,4]))
