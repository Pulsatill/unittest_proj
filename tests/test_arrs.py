import unittest
from utils import arrs
from utils import dicts


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([], -1, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([], 1, -1), [])
        self.assertEqual(arrs.my_slice([-1, 0, 1, 2], 1), [0, 1, 2])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -1, 3), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -5, 4), [1, 2, 3, 4])


class TestDicts(unittest.TestCase):

    def test_dict(self):
        self.assertEqual(dicts.get_val({"vcs": "mercurial"}, "vcs"), "mercurial")
        self.assertEqual(dicts.get_val({"vcs": "mercurial"}, "vcs", "git"), "mercurial")
        self.assertEqual(dicts.get_val({}, "vcs", "git"), "git")
        self.assertEqual(dicts.get_val({}, "vcs", "bazaar"), "bazaar")
