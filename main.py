from Pipeline import Pipeline
from ModelAnalysis import ModelAnalysis
from ModelPlots import ModelPlots
from colabcode import ColabCode
from tests import TestInputDataShape
import unittest



if __name__ == '__main__':
    N, h, w, c = 5, 10, 10, 2
    PL = Pipeline()
    PL.get_uwind_and_vwind_data()
    unittest.main()
