#!/usr/bin/python3
from sklearn.datasets import load_iris
from sklearn import tree
import graphviz

iris=load_iris()

clf=tree.DecisionTreeClassifier()

tree.export_graphviz(clf,
					out_file=None,
					feature_names=iris.feature_names,
					class_names=iris.target_names)