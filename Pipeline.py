import numpy as np
import os
import netCDF4 as nc
from netCDF4 import Dataset
# import tensorflow as tf
import time

class Pipeline:
    def __init__(self, N, h , w):
        self.N = N
        self.h = h
        self.w = w

    def create_wind_nc_files(self, wsfilepath=('./ncFiles/small_ws.nc'), wdfilepath=('./ncFiles/small_wd.nc')):
        '''
        creates 2 files for ws/wd
        adds columns for time, lat, long, ws, wd
        fills in arbitrary data for these 2 files
        '''
        columns = {'time': 20,
                   'lat': 10,
                   'lon': 10,
                   'ws': 100,
                   'wd': 100
                   }

        if os.path.exists(wsfilepath):
            print('Found Previously Created nc Files')
            # return
        else:
            try:
                with nc.Dataset(wsfilepath, mode='w', format='NETCDF4_CLASSIC') as ws_nc, nc.Dataset(wdfilepath, mode='w', format='NETCDF4_CLASSIC'):
                    print('Succesfully Created new nc files')
                    os.chmod(wsfilepath, 0o666)
                    os.chmod(wdfilepath, 0o666)
                    
                    ws_time_dim = ws_nc.createDimension('time', columns['time'])
                    ws_lat_dim = ws_nc.createDimension('lat', columns['lat'])
                    ws_lon_dim = ws_nc.createDimension('lon', columns['lon'])
                    ws_ws_dim = ws_nc.createDimension('ws', columns['ws'])

                    wd_time_dim = wd_nc.createDimension('time', columns['time'])
                    wd_lat_dim = wd_nc.createDimension('lat', columns['lat'])
                    wd_lon_dim = wd_nc.createDimension('lon', columns['lon'])
                    wd_wd_dim = wd_nc.createDimension('wd', columns['ws'])

            except FileNotFoundError as e:
                print('File not found!')
                return
        
        ws_nc = nc.Dataset(wsfilepath)
        wd_nc = nc.Dataset(wdfilepath)

        # Initalize Dimensions First
        # time_dim = ws_nc.createDimension('time', columns['time'])
        # # lat_dim = 
        # print(ws_nc)



    def create_ones_numpy_tensor(self, c):
        np_tensor = np.ones([self.N, self.h, self.w, c])

        assert np_tensor.shape == (self.N, self.h, self.w, c)

        return np_tensor
    

    ## 2D Variables
    def get_uwind_and_vwind(self, C=2):
        '''
            Open wind_speed.nc and wind_direction.nc files
            Converts data from speed and directiton to u and v components
            Creates [N, h, w, 2] numpy tensor and converts into TFRecord

            Saves TFRecord to ./Data/TFRecord_data
        '''
        return self.create_ones_numpy_tensor(C)
    
    def get_DNI_and_DHI(self, C=2):
        '''
            Open solar.nc files
            Creates [N, h, w, 2] numpy tensor and converts into TFRecord

            Saves TFRecord to ./Data/TFRecord_data
        '''
        return self.create_ones_numpy_tensor(C)

    def get_geopotential(self, C=3):
        '''
            open geopotential.nc
            Creates [N, h, w, 3] numpy tensor and converts into TFRecord
            C = 3 corresponds to Altitude Levels = 850, 700, 500 hPa
            
            Saves TFRecord to ./Data/TFRecord_data
        '''
        return self.create_ones_numpy_tensor(C)

    def get_specific_humidity(self, C=3):
        '''
            open specific_humidity.nc
            Creates [N, h, w, 3] numpy tensor and converts into TFRecord
            C = 3 corresponds to Altitude Levels = 850, 700, 500 hPa
            
            Saves TFRecord to ./Data/TFRecord_data
        '''
        return self.create_ones_numpy_tensor(C)

    def get_temperature(self, C=3):
        '''
            open temperature.nc
            Creates [N, h, w, 3] numpy tensor and converts into TFRecord
            C = 3 corresponds to Altitude Levels = 850, 700, 500 hPa
            
            Saves TFRecord to ./Data/TFRecord_data
        '''
        return self.create_ones_numpy_tensor(C)

    def get_sealevel_pressure(self, C=1):
        '''
            open sealevel_pressure.nc
            Creates [N, h, w, 1] numpy tensor and converts into TFRecord
            C = 3 corresponds to Altitude Levels = 850, 700, 500 hPa
            
            Saves TFRecord to ./Data/TFRecord_data
        '''
        return self.create_ones_numpy_tensor(C)

    def get_total_aerosol_optical_depth_forcing(self, C=1):
        '''
            open total_aerosol_optical_depth_forcing.nc
            Creates [N, h, w, 1] numpy tensor and converts into TFRecord
            C = 3 corresponds to Altitude Levels = 850, 700, 500 hPa
            
            Saves TFRecord to ./Data/TFRecord_data
        '''
        return self.create_ones_numpy_tensor(C)
    
    ## 1D variables
