# AI Spam Classifier

## Overview

This project is a simple AI-based text classifier built using Python and Scikit-learn. It classifies user-entered messages as either Spam or Not Spam.

## Features

* Accepts user input
* Processes text using Machine Learning
* Predicts whether a message is spam or normal
* Console-based interface

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib

## Project Structure

ai-spam-classifier/

* train.py
* app.py
* spam.csv
* model.pkl
* vectorizer.pkl
* README.md
* requirements.txt

## Installation

Install required packages:

pip install pandas scikit-learn joblib

## Run the Project

Train the model:

py train.py

Run the classifier:

py app.py

## Example

Input:
Congratulations! You won ₹50,000

Output:
Spam Message Detected
