from runner.koan import *
from numpy import zeros

class AboutZeros(Koan):

    def test_zeros(self):
        numpy_zeros = zeros([[1,2],[3,4]])
        self.assertEquals(__, numpy_zeros.tolist())

    def test_zeros_from_int(self):
        numpy_zeros = zeros(5)
        self.assertEquals(__, numpy_zeros.tolist())

    def test_zeros_specifying_type(self):
        numpy_zeros = zeros([2,3], dtype=float)
        self.assertEquals(__, numpy_zeros.tolist())

    def test_zeros_from_tuple(self):
        numpy_zeros = zeros((2,2))
        self.assertEquals(__, numpy_zeros.tolist())