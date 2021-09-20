# Flight Fare Prediction 
## Problem Statement:
Travelling through flights has become an integral part of today’s lifestyle as more and more people are opting for faster travelling options. The flight ticket prices increase or decrease every now and then depending on various factors like timing of the flights, destination, and duration of flights various occasions such as vacations or festive season. Therefore, having some basic idea of the flight fares before planning the trip will surely help many people save money and time.

## Approach:
The main goal is to predict the fares of the flights based on different factors available in the dataset.

1.Data Exploration     : I started exploring dataset using pandas,numpy,matplotlib and seaborn. <br>
2.Data visualization   : Ploted graphs to get insights about dependend and independed variables. <br>
3.Feature Engineering  : Removed missing values and created new features as per insights.<br>
4.Model Selection I    : Tested all base models to check the base accuracy.<br>
                         Also ploted residual plot to check whether a model is a good fit or not.<br>
5.Model Selection II   :  Performed Hyperparameter tuning using gridsearchCV and randomizedSearchCV.<br>
6.Pickle File          :  Selected model as per best accuracy and created pickle file using joblib .<br>
7.Webpage & deployment :  Created a webform that takes all the necessary inputs from user and shows output.<br>
                                After that I have deployed project on google cloud as well as on heroku platform.<br>
                               
## Deployment Links:
Heroku link:https://flight-fare-prediction1301.herokuapp.com/
## User Interface:
![Capture](https://user-images.githubusercontent.com/63538576/132983915-1bad4b43-9ecc-4315-8ea1-bed335c5b898.JPG)

## Technologies Used:
1. Python 
2. Sklearn
3. Flask
4. Html
5. Css
6. Pandas, Numpy 
7. Database 
8. Hosting

## Technical aspect:
1.Python 3.9<br>
2.Front-end: HTML, CSS<br>
3.Back-end: Flask<br>
4.IDE: Jupyter Notebook, VisualStudio<br>
5.Database: MongoDB Atlas<br>
6.Deployment: Heroku<br>

## Run Locally
1.Clone the project<br>
  git clone https://github.com/Poojasharma1301/iNeuron_internship<br>
2.Go to the project directory<br>
  cd iNeuron_Internship<br>
3.Install dependencies<br>
  pip install -r requirements.txt<br>
4.Setting up the Controllers files<br>
    Update the values inside the Controllers folder<br>
5.Run the app.py<br>
  python app.py<br>

## Help Me Improve
Hello Reader if you find any bug please consider raising issue I will address them asap.

