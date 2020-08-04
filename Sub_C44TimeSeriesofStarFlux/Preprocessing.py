#read train data
import sys
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.preprocessing import StandardScaler

from C44TimeSeriesofStarFlux.Sub_C44TimeSeriesofStarFlux.KalmannFilter import Simple_Kalman

class Dataset():
    def __init__(self):
        # read csv data as frame
        self.path = Path(r'D:/datasets/exoplanets')
        self.path = list(self.path.glob('*'))[1]
        print('windowspath:', self.path)

    def readcsv(self):
        # read csv data as frame
        print('windowspath:', self.path)
        self.data = pd.read_csv(self.path, delimiter=',')
        #return(self.data)

    def groupdivision(self):
         # divied the dataframe into two groups
         self.data1 = self.data[self.data.LABEL < 2]
         self.data2 = self.data[self.data.LABEL > 1]
         print('confirmed exoplanet-stars:', self.data2.shape, 'non-exoplanet-stars:', self.data1.shape)
         print(len(self.data2.index), len(self.data1.index))
         print(self.data2.index)
         #return(self.data1, self.data2)

    def data2denoise(self):
        print('==>processing')
        for i in range(0, len(self.data2.index)):
            # reshape 2d->1d
            self.df2 = self.data2.loc[i]
            self.df22 = self.df2.values
            self.df222 = self.df22.reshape(len(self.df22), -1)
            # print(self.df22.shape, self.df222.shape)
            # normalization
            self.scalar = StandardScaler()
            self.data_stand2 = self.scalar.fit_transform(self.df222)
            self.observed_position = self.data_stand2.reshape(len(self.df22))
            # print(self.observed_position.shape)
            # return (self.observed_position)

            kf = Simple_Kalman(self.observed_position, 0, 1, 1, 100)

            # plt.plot(timeseries,data_stand2,color='blue')
            plt.figure(figsize=(15, 5))

            plt.xlabel('time')
            plt.ylabel('FLUX: indensity of light')
            # plt.plot(true_position, 'r--', label='True Positions')
            plt.plot(self.observed_position, 'y', label='Observed Positions')
            plt.plot(kf.x_, color='blue', label='Foward Estimation')
            # plt.plot(kf.x_all_, 'black', label='Smoothed Estimation')
            plt.legend(loc='best')














if __name__ == "__main__":
    print(sys.path)
    print('==>Preprocessing imported')

