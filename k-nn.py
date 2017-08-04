import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')
import warnings
import pandas as pd
import random
dataset={'k':[[1,2],[2,3],[4,2]],'r':[[7,6],[5,4],[8,9]]}
new_feature=[5,6]


def k_nearest(data,predictn,k):
	if len(data)>=k:
		warnings.warn("k is set less than total voting groups")
	else:
		dist=[]
		for group in data:
			for feature in data[group]:
				eucld_dist=np.linalg.norm(np.array(feature)-np.array(predictn))
				dist.append([eucld_dist,group])
		votes=[i[1] for i in sorted(dist)[:k]]
		vote_res=Counter(votes).most_common(1)[0][0]
		return vote_res
		
def get_apply_data():
	lst=['id_number','Clump_Thickness','Unif_of_cell_size','Unif_of_cell_shape','Marginal_Adhesion','Single_epith_cell_size'
	,'Bare_nuclei','Bland_Chromatin','Normal_nuclei','Mitoses','Class']
	dat=pd.read_table("data.txt",header=None,sep=',',names=lst)
	#print(dat.head())
	dat.replace('?',-99999,inplace=True)
	dat.drop(['id_number'],1,inplace=True)
	full_data=dat.astype(float).values.tolist()
	print(full_data[:10])
	random.shuffle(full_data)
	test_size=0.3
	train_set={2:[],4:[]}
	test_set={2:[],4:[]}
	train_data=full_data[:-int(len(full_data)*test_size)]
	test_data=full_data[-int(len(full_data)*test_size):]
	for k in train_data:
		train_set[k[-1]].append(k[:-1])
	
	for m in test_data:
		test_set[m[-1]].append(m[:-1])
		
		
	correct=0
	total=0
	for grp in test_set:
		for data in test_set[grp]:
			vote=k_nearest(train_set,data,5)
			if grp==vote:
				correct+=1
			total+=1
			
	acc=correct/total
	print("accuracy:{}".format(acc))
get_apply_data()


		
#ans=k_nearest(dataset,new_feature)
#print(ans)
'''for i in dataset:
	for k in dataset[i]:
		plt.scatter(k[0],k[1],s=100,color=i)
plt.scatter(new_feature[0],new_feature[1],color=ans)
plt.show()'''
	

	