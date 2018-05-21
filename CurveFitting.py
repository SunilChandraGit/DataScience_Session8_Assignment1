import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

#Initialize min. and max. temperatures in different cities
temp_max = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27,  25])
temp_min = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])

#define function returning the optimized curve fit
def yearly_temps(times, avg, ampl, time_offset):
    return (avg
            + ampl * np.cos((times + time_offset) * 2 * np.pi / times.max()))

#intialize months numpy array for months from 1-12
months = np.arange(12)

#get the optimal values and covariance for min and max temperatures
res_max, cov_max = optimize.curve_fit(yearly_temps, months,
                                      temp_max, [20, 10, 0])
res_min, cov_min = optimize.curve_fit(yearly_temps, months,
                                      temp_min, [-40, 20, 0])

#initialize days with numpy array of 365 values between 0 to 12
days = np.linspace(0, 12, num=365)

#Plot the figure for min and max temperature
plt.figure()
plt.plot(months, temp_max, 'ro')
plt.plot(days, yearly_temps(days, *res_max), 'r-')
plt.plot(months, temp_min, 'bo')
plt.plot(days, yearly_temps(days, *res_min), 'b-')
plt.xlabel('Month')
plt.ylabel('Temperature ($^\circ$C)')

plt.show()
