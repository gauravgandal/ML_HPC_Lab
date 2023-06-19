import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Load dataset
dataset=pd.read_csv("hw.csv")
# To display dataset
print(dataset)
x=dataset.iloc[:,:-1].values
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values
print(X)
print(y)
#from sklearn subpackage import linear regression model
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,y)
#To get the slop
regressor.coef_
#To get the y intercept
regressor.intercept_
#To print the equation of line
print("y= "+ str(regressor.coef_) + "X + " + str(regressor.intercept_))

#To get the slop
print("Accuracy:",regressor.score(X,y)*100)
#To plot graph
plt.plot(X,y,'o')
plt.plot(X,regressor.predict(X));
plt.show()
predict_x=int(input('Enter Height:'))
predict_y=(0.67461045*predict_x)-38.45508707607698
plt.scatter(X,y)
plt.scatter(predict_x,predict_y)
plt.xlabel('Enter Height:(Predicted_x)')
plt.ylabel('Enter Weight:(Predicted_y)')
#plotting the Predicted regression line
plt.plot(X,regressor.predict(X),color='green');
plt.show()
