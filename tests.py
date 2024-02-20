import unittest
import numpy as np
from Pipeline import Pipeline
from Models import Models

class TestInputDataShape(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.N = 20
        self.h = 10
        self.w = 5

    def test_phiregan_shape(self):
        tensor = Models(self.N, self.h, self.w)
        tensor = tensor.stengal_2dtensor_shape
        expected_shape = (self.N, self.h, self.w, 2)
        self.assertEqual(tensor, expected_shape, 'phiregan shape wrong')

    def test_doury_2d_shape(self):
        tensor = Models(self.N, self.h, self.w)
        tensor = tensor.doury_2dtensor_dim
        expected_shape = (self.N, self.h, self.w, 19)
        self.assertEqual(tensor, expected_shape, 'doury 2d shape wrong')

    def test_doury_1d_shape(self):
        tensor = Models(self.N, self.h, self.w)
        tensor = tensor.doury_1dtensor_dim
        expected_shape = (self.N, 1, self.w, 5)
        self.assertEqual(tensor, expected_shape, 'phiregan 1d shape wrong')


