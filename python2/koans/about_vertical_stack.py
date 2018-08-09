from runner.koan import *
from numpy import array
from numpy import vstack

class AboutVerticalStack(Koan):

    def test_vstack(self):
        first_array = array([3,4])
        second_array = array([1,2])
        self.assertEquals(__, vstack((first_array, second_array)))

    def test_vstack_shape(self):
        first_array = array([3,4])
        second_array = array([1,2])
        self.assertEquals(__, vstack((first_array, second_array)).shape)        