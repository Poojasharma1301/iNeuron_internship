# Flight Fare Prediction 
## Problem Statement:
Travelling through flights has become an integral part of today’s lifestyle as more and more people are opting for faster travelling options. The flight ticket prices increase or decrease every now and then depending on various factors like timing of the flights, destination, and duration of flights various occasions such as vacations or festive season. Therefore, having some basic idea of the flight fares before planning the trip will surely help many people save money and time.

## Approach:
The main goal is to predict the fares of the flights based on different factors available in the dataset.

1.Data Exploration     : I started exploring dataset using pandas,numpy,matplotlib and seaborn. 
2.Data visualization   : Ploted graphs to get insights about dependend and independed variables. 
3.Feature Engineering  : Removed missing values and created new features as per insights.
4.Model Selection I    : Tested all base models to check the base accuracy.<br>
                         Also ploted residual plot to check whether a model is a good fit or not.
5.Model Selection II   :  Performed Hyperparameter tuning using gridsearchCV and randomizedSearchCV.
6.Pickle File          :  Selected model as per best accuracy and created pickle file using joblib .
7.Webpage & deployment :  Created a webform that takes all the necessary inputs from user and shows output.
                                After that I have deployed project on heroku platform.
