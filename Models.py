from typing import *
from Pipeline import Pipeline

class Models:
    def __init__(self, N: int, h: int, w: int) -> None:
        '''
            Defines inital shape of each model

            Args:
                N (int): batch size
                h (int): image pixel height
                w (int): image pixel width
        '''
        self.N = N
        self.h = h
        self.w = w

        ## Stengal Variables
        self.stengal_2dfeatures_dim = 2
        self.stengal_2dtensor_shape = (N, h, w, self.stengal_2dfeatures_dim)

        ## Doury Variables
        self.doury_2dfeatures_dim = 19
        self.doury_1dfeatures_dim = 5

        self.doury_2dtensor_dim = (N, h, w, self.doury_2dfeatures_dim)
        self.doury_1dtensor_dim = (N, 1, w, self.doury_1dfeatures_dim)

    def fetch_stengal_wind_data():
        PL = Pipeline()
       
        PL.get_uwind_and_vwind_data()
