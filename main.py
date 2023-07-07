#Import python modules
import matplotlib.pyplot as plt
import numpy as np
import time

#Create variables
x_val = []
a_val = []
a = 1

print("This script will be creating a simple bifurcation logistic map.")

time.sleep(1)

print("Once the graph is generated it will display on the screen and be saved.")

while a < 4:
    xold = 0.5
    
    #Ignore first 100 iterations to get to steady-state
    for i in range(100):
        xnew = (a*xold)*(1-xold)
        xold = xnew
   
   #These are the results to record 
    for i in range(100):
        xnew = (a*xold)*(1-xold)
        xold = xnew
        a_val.append(a)
        x_val.append(xnew)

    a+=0.001
z = np.arange(len(a_val))

# Define the colormap
cmap = plt.get_cmap('jet')

#Create plot with recorded data
plt.scatter(a_val, x_val, s = 0.1, c=z, cmap=cmap)
plt.xlabel("a")
plt.ylabel("x")
plt.title("Bifurcation Logistic Map")
plt.savefig('bifurcation-logisitic-map.png')
plt.show()

time.sleep(1)
print("Graph was saved as 'bifurcation-logisitic-map.png'. Thank you!")

