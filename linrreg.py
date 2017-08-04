import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean

xs=np.array([1,2,3,4,5],dtype=np.float64)
ys=np.array([5,4,6,7,6],dtype=np.float64)

def bst_fit_slope(xs,ys):
	
	m=((mean(xs)*mean(ys)-mean(xs*ys))/((mean(xs)*mean(xs))-mean(xs*xs)))
	b=mean(ys)-m*mean(xs)
	return m,b
	
m,b=bst_fit_slope(xs,ys)
print(m,b)
predict_x=7
predict_y=m*predict_x+b
regr_line=[(m*x)+b for x in xs]
plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y)
plt.plot(xs,regr_line)
plt.show()