import numpy as np
import matplotlib.plot as plt
import math

class Support_Vector_Machine(object):
	def __init__(self,viz=True):
		self.viz=viz
		self.colors={1:'r',-1:'b'}
		if self.viz:
			self.fig=plt.figure()
			self.ax=self.add_subplot(1,1,1)
	
	def fit(self,data):
	#optimization problem here svm
		self.data=data
		temp_dict={}
		transforms=[[1,1],
					[-1,1],
					[-1,-1],
					[1,-1]]
					
		all_data=[]
		for y in self.data:
			for featureset in self.data[y]:
				for feature in featureset:
					all_data.append(feature)
		self.max_feature_value=max(all_data)
		self.min_feature_value=min(all_data)
		all_data=None
		#expensive step is 0.001
		step_sizes=[self.max_feature_value*0.1,
					self.max_feature_value*0.01,
					self.max_feature_value*0.001]
		b_range_multiple=5
		
		b_multiple=5
		latest_optimum=self.max_feature_value*10
		
		for step in step_sizes:
			w=np.array([latest_optimum,latest_optimum])
			optimized=False
			while not optimized:
				pass
		
	def predict(self,features):
		classify=np.sign(np.dot(features,self.w)+self.b)
		return classify
		



data_dict={-1:np.array([[1,7],[2,8],[3,8]]),1:np.array([[5,1],[6,-1],[7,3]])}
