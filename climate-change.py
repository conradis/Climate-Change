import matplotlib as mpl
mpl.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('1880-2017.csv', delimiter=',', dtype=None, skip_header=5, names=('Year', 'Value'))

plt.title('Anomalia della temperatura')
plt.xlabel('Anno')
plt.ylabel('Gradi Celsius +/- rispetto alla media')
plt.bar(data['Year'], data['Value'], color='blue')
plt.show()