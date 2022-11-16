import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('imu_data1.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    
    next(plots)
    for row in plots:
        x.append(row[0])
        y.append(float(row[10]))
  
plt.plot(x, y)
plt.legend()
plt.show()