#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
### it's all yours from here forward!  
from sklearn import tree
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.cross_validation import train_test_split


clf = tree.DecisionTreeClassifier()
features_train, features_test, labels_train, labels_test = \
                    train_test_split(features, labels, test_size=0.3, random_state=42)
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

print "Accuracy ", accuracy_score(pred, labels_test)

print "No of POIs predicted in the test set ", len(list(filter(lambda x:x==1.0, pred)))
print "Total no of people test set", len(labels_test)
print "Accuracy if all zero predicted", accuracy_score([0 for i in range(29)], labels_test)
print "No of True positives ", sum([pred[i] == labels_test[i] and pred[i] == 1 for i in range(len(labels_test))])

print "Precision Score ", precision_score(pred, labels_test)
print "Recall Score ", recall_score(pred, labels_test) 

