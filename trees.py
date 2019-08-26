import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

loans = pd.read_csv('loan_data.csv')

print(loans.info())
print(loans.describe())
print(loans.head())

# Data Exploration
plt.figure(figsize=(10,6))
loans[loans['credit.policy']==1]['fico'].hist(alpha=0.5,color='blue',bins=30,label = 'Credit.Policy=1')

loans[loans['credit.policy']==0]['fico'].hist(alpha=0.5,color='red',bins=30,label = 'Credit.Policy=0')
plt.legend()
plt.xlabel('FICO')
plt.show()


plt.figure(figsize=(10,6))
loans[loans['not.fully.paid']==1]['fico'].hist(alpha=0.5,color='blue',bins=30,label = 'not.fully.paid=1')

loans[loans['not.fully.paid']==0]['fico'].hist(alpha=0.5,color='red',bins=30,label = 'not.fully.paid=0')
plt.legend()
plt.xlabel('FICO')
plt.show()

plt.figure(figsize=(11,7))
sns.countplot(x='purpose',hue='not.fully.paid',data=loans,palette='Set1')
plt.show()

sns.jointplot(x='fico',y='int.rate',data=loans,color='purple')
plt.show()

# Data Transformation
cat_feats = ['purpose']

final_data = pd.get_dummies(loans,columns=cat_feats,drop_first=True)

print(final_data.info())

# Training
from sklearn.model_selection import train_test_split

x = final_data.drop('not.fully.paid',axis=1)
y = final_data['not.fully.paid']
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.30,random_state=101)

from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier()

dtree.fit(x_train,y_train)

predictions = dtree.predict(x_test)

from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))

# Random Tree

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()

rfc.fit(x_train,y_train)

predictions = rfc.predict(x_test)

print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))