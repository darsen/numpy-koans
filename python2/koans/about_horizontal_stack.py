from runner.koan import *
from numpy import array
from numpy import hstack

class AboutHorizontalStack(Koan):

    def test_hstack(self):
        first_array = array((1,2,3)
        second_array = array((4,5,6)
        self.assertEquals(__, hstack((first_array, second_array)))

    def test_hstack_shape(self):
        first_array = array([[1],[2],[3]])
        second_array = array([[6],[5],[4]])
        self.assertEquals(__, hstack((first_array, second_array)).shape)        