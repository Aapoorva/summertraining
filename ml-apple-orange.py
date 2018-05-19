#!/usr/bin/env python3
from sklearn import tree
import sys

data=sys.argv
wgt=int(data[1])
txtre=int(data[2])

#		   wgt txtre
features=[[110,0],[140,0],[120,0],[80,1],[90,1],[100,1]]

output=["Apple","Apple","Apple","Orange","Orange","Orange"]

algo=tree.DecisionTreeClassifier()

trained=algo.fit(features,output)

output=trained.predict([[wgt,txtre]])

print(output)