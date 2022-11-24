from matplotlib import pyplot as plt
from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import train_test_split
import os
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.tree import export_graphviz
import graphviz


def unique(list1):
    x = np.array(list1)
    print(np.unique(x))


cwd = os.getcwd()
features, labels = load_svmlight_file(cwd + "/Teste_1/data/data")
# print(features)
unique(labels)

x, X_test, y, y_test = train_test_split(features, labels, test_size=0.3333, stratify=labels)
X_train, X_cv, y_train, y_cv = train_test_split(x, y, test_size=0.5, train_size=0.5, stratify=y)

clf = DecisionTreeClassifier(max_depth=4)
clf.fit(X_train, y_train)

# plot tree
fig = plt.figure(figsize=(40, 20))
tree.plot_tree(clf, fontsize=10, filled=True)
fig.savefig("decision_tree.png")
fig.show()

# dot_data = export_graphviz(clf, filled=True, rounded=True, out_file=None) # No Windows existe problema no graphiz
# graph = graphviz.Source(dot_data, format="png")
# graph.save('tree.png')

# python3 ./Users/fhod/PycharmProjects/Trabalho_pcc170_parametros/acviz-master/acviz.py --iracelog /Users/fhod/PycharmProjects/Trabalho_pcc170_parametros/Teste_1/irace_1/irace.Rdata
os.system(f"{cwd}/acviz-master/acviz.py --iracelog {cwd}/Teste_1/irace_1/irace.Rdata")

os.system(f"{cwd}/acviz-master/acviz.py --iracelog {cwd}/Teste_2/irace_1/irace.Rdata")
# python3 ./acviz-master/acviz.py --iracelog /Users/fhod/PycharmProjects/Trabalho_pcc170_parametros/Teste_1/irace_1/irace.Rdata
# python3 ./acviz-master/acviz.py --iracelog /Users/fhod/PycharmProjects/Trabalho_pcc170_parametros/Teste_2/irace_1/irace.Rdata