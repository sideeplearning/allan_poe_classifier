class Visual(Dataset):
    def __init__(self):
        self.timeseries = np.arange(3198)

    def plot(self):
        # plt.plot(timeseries,data_stand2,color='blue')
        plt.figure(figsize=(15, 5))
        plt.title(i)
        plt.xlabel('time')
        plt.ylabel('FLUX: indensity of light')
        # plt.plot(true_position, 'r--', label='True Positions')
        plt.plot(timeseries, observed_position, 'y', label='Observed Positions')
        plt.plot(kf.x_, color='blue', label='Foward Estimation')
        # plt.plot(kf.x_all_, 'black', label='Smoothed Estimation')
        plt.legend(loc='best')
        # print(df2.name)
