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



class TestPipelineDataShape(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.N = 20
        self.h = 10
        self.w = 5

    def test_get_uwind_and_vwind_shape(self):
        PL = Pipeline(self.N, self.h, self.w)
        tensor = PL.get_uwind_and_vwind()
        expected_shape = (self.N, self.h, self.w, 2)
        self.assertEqual(tensor.shape, expected_shape, 'uwind/vwind shape wrong')

    def test_get_DNI_and_DHI_shape(self):
        PL = Pipeline(self.N, self.h, self.w)
        tensor = PL.get_DNI_and_DHI()
        expected_shape = (self.N, self.h, self.w, 2)
        self.assertEqual(tensor.shape, expected_shape, 'DNI/DHI shape wrong')


    def test_get_geopotential_shape(self):
        PL = Pipeline(self.N, self.h, self.w)
        tensor = PL.get_geopotential()
        expected_shape = (self.N, self.h, self.w, 3)
        self.assertEqual(tensor.shape, expected_shape, 'geopotential shape wrong')

    def test_get_specific_humidity_shape(self):
        PL = Pipeline(self.N, self.h, self.w)
        tensor = PL.get_specific_humidity()
        expected_shape = (self.N, self.h, self.w, 3)
        self.assertEqual(tensor.shape, expected_shape, 'specific humidity shape wrong')

    def test_get_temperature_shape(self):
        PL = Pipeline(self.N, self.h, self.w)
        tensor = PL.get_temperature()
        expected_shape = (self.N, self.h, self.w, 3)
        self.assertEqual(tensor.shape, expected_shape, 'temperature shape wrong')

    def test_sealevel_pressure_shape(self):
        PL = Pipeline(self.N, self.h, self.w)
        tensor = PL.get_sealevel_pressure()
        expected_shape = (self.N, self.h, self.w, 1)
        self.assertEqual(tensor.shape, expected_shape, 'sealevel shape wrong')
    
    def test_total_aerosol_optical_depth_forcing_shape(self):
        PL = Pipeline(self.N, self.h, self.w)
        tensor = PL.get_total_aerosol_optical_depth_forcing()
        expected_shape = (self.N, self.h, self.w, 1)
        self.assertEqual(tensor.shape, expected_shape, 'totol aerosol optical depth forcing shape wrong')