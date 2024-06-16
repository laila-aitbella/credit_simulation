
# Credit Simulation App

The Credit Simulation App is a web application designed to predict credit approval status based on user inputs. The app utilizes a machine learning model to analyze credit history, marital status, and applicant income to determine whether a user's credit application will be approved or denied.

## Table of Contents

- [Overview](#overview)
- [Project Steps Summary](#project-steps-summary)
- [Features](#features)
- [Technologies Used](#technologies-used)

## Overview

The Credit Simulation App provides a simple and intuitive interface for users to input their credit-related information and get an immediate prediction on their credit approval status. This tool can be particularly useful for individuals looking to assess their eligibility for loans or other credit products.

## Project Steps Summary
### Loading Data:
The data is imported from a CSV file into a pandas DataFrame.
### Selecting Relevant Columns:
Among all available features, only the columns Credit_History, Married, and ApplicantIncome are selected for analysis.
### Splitting Data into Training and Test Sets: 
The data is split into training and test sets using the StratifiedShuffleSplit method. This method ensures that the class distribution is maintained in both sets, ensuring an equitable distribution.
### Training the Logistic Regression Model:
A logistic regression model is trained on the training set. This model is chosen for its simplicity and effectiveness in binary classification problems.
### Evaluating the Model:
The performance of the model is evaluated on the test set.
### Saving the Model:
The trained model is saved to a file using the pickle library. This allows the model to be preserved for future deployment without having to retrain it.
### Loading the Model and Making Predictions:
The saved model is loaded from the file and used to make predictions on new data. This step demonstrates how the model can be deployed and used in real-world applications.

## Features

- **User Input Form**: A form for users to input their credit history, marital status, and coapplicant income.
- **Machine Learning Prediction**: Uses a pre-trained machine learning model to predict credit approval.
- **Result Display**: Shows whether the credit is approved or denied based on the input data.
- **User-Friendly Interface**: Simple and easy-to-use web interface.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Machine Learning**: scikit-learn, pickle

