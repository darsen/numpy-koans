from runner.koan import *
from numpy import ones

class AboutOnes(Koan):

    def test_ones(self):
        numpy_ones = ones([[3,2],[3,4]])
        self.assertEquals(__, numpy_ones.tolist())

    def test_ones_from_int(self):
        numpy_ones = ones(3)
        self.assertEquals(__, numpy_ones.tolist())

    def test_ones_specifying_type(self):
        numpy_ones = ones([7,1], dtype=float)
        self.assertEquals(__, numpy_ones.tolist())

    def test_ones_from_tuple(self):
        numpy_ones = ones((1,2))
        self.assertEquals(__, numpy_ones.tolist())