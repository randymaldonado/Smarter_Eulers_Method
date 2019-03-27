import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 
import timeit

start = timeit.default_timer()

def diff_eq(x,y):
	'''
	This function defines our DE, allowing us to change equations easily.
	'''

	# DE #1
	# d = (np.exp(x) * np.sin(y)/np.cos(x))

	# DE #2
	d = (np.exp(x) * np.sin(y))
	return d

def calculations(x,y,delta):
	'''
	Performs calculations for differential equation using eulers method.
	Inputs are all floats.
	x = x_k
	y = y_k
	delta = delta x
	'''
	# Step 1: Calculate dy/dx = f(x_k,y_k) using the given DE.
	f_k = diff_eq(x,y)

	# Step 2: Calculate t_{k+1} and y_{k+1} using normal euler's method.
	x_k1 = x + delta
	y_k1 = y + delta * f_k

	# Step 3: Calculate dy/dx = f(x_{k+1}, y_{k+1}).
	f_k1 = diff_eq(x_k1,y_k1)

	return x_k1, y_k1, f_k, f_k1

def check_distance(fk, fk1):
	'''
	This function will check the distane between 
	dy/dx(x_k,y_k) and dy/dx(x_{k+1},y_{k+1}).
	If the distance is ok, it will proceed to reutrn the values that will be appended.
	If not good, the function will run again with a new delta.

	Returns a true or false.
	'''
	dist = np.abs(fk1 - fk)
	# this paramater is what we must optimize in order to run fast and keep accuracy.
	p = .1

	if dist > p:
		return True

	else:
		return False

def smart_eulers_method(x,y,delta,xend):
	'''
	Here x and y are lists. 
	'''

	i=0
	while x[i] < xend:
		x_k1, y_k1, f_k, f_k1 = calculations(x[i],y[i],delta)
		delt = delta/10

		while check_distance(f_k, f_k1):
			x_k1, y_k1, f_k, f_k1 = calculations(x[i],y[i],delt)
			delt = delt/10

		x.append(x_k1)
		y.append(y_k1)
		i+=1


	d = {"y" : y}
	df = pd.DataFrame(d, index=x)
	return df

x = [0]
y = [1]
xend = 10
delta = .1

df = smart_eulers_method(x, y , delta, xend)
stop = timeit.default_timer()
print(df)
print(stop - start)
plt.plot(df)
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("New Euler's Method")
plt.show()








