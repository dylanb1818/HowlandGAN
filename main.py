from Pipeline import Pipeline

if __name__ == '__main__':
    N, h, w, c = 5, 10, 10, 2


    PL = Pipeline
    PL.create_wind_nc_files()
    np_tensor = PL.create_ones_numpy_tensor(1, 3, 3, 2)
    print(np_tensor)