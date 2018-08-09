from runner.koan import *
from numpy import array

class AboutArrays(Koan):

    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        # Confused? This video should help:
        #
        #   http://bit.ly/about_asserts

        self.assertTrue(True)  # This should be True

    def test_array_to_numpy_array_and_back(self):
        numpy_array = array([[1,2],[3,4]])
        self.assertEquals(__, list(reversed(numpy_array.tolist())))

    def test_array_shape(self):
        numpy_array = array([1,2])
        self.assertEquals(__, numpy_array.shape)

    def test_array_dtype(self):
        numpy_array = array([1.0, 2.0])
        self.assertEquals(__, numpy_array.dtype)

    def test_array_dtype(self):
        numpy_array = array([1.0, 2.0])
        self.assertEquals(__, numpy_array.dtype)

    def test_array_type(self):
        numpy_array = array([1.0, 2.0])
        self.assertEquals(__, type(numpy_array))