# Generating independent standard normally distributed random number 
# using Box-Müller Method.

from random import random as ran
from math import sqrt, log, pi, cos, sin
from statistics import mean, stdev

def gaussianRand(mu, sigma):
	""" Two independent uniformly distributed random variables xi1 and xi2 become 
	two independent Gaussian distributed variables Xf and Yf under Box-Müller 
	Transformation.
	"""
	xi1, xi2 = ran(), ran()
	Xf, Yf = sqrt(-2*log(xi1))*cos(2*pi*xi2), sqrt(-2*log(xi1))*sin(2*pi*xi2)
	return(mu + sigma*Xf)
	# print("Xf=",Xf,"Yf=",Yf)

# Test
gRandList = [ ]
mu_in = float(input("mu = "))
sigma_in = float(input("sigma = "))
output_length = int(input("output length = "))
for k in range(1, output_length):
	gRandList.append(gaussianRand(mu_in, sigma_in))
print("The mean value of the output list is %.5f ."%mean(gRandList))
print("The standard deviation of the output list is %.5f ."%stdev(gRandList))
input()
