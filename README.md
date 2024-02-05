
# Real-time Fault Detection and Localization with AI

## Powering smarter grids.

This web app is capable of detecting a fault in a transmission lines and its location when provide with live data consisting of features such as Current,Voltage and Rmscurrent etc. 

# File Structure

## Assets

This Folder consists of three models :-
1. **ann.ipynb**: This is deep learning model we trained to check     weather check its accuracy and compare it against machine learning algorithms.


2. **detect_model**: This is machine learning model which is trained to detect the type of fault that has occured in transmission line (such as AG - A to ground).

3. **localization**: This is a model which predicts the distance  at which the fault has occured.

## Models 
This File contains all the weights of trained model.

## Simulation Data 
This is file consists of data which we are going to use for demonstration and send it as live readings to our model.

## Static
This folder consists of static files such as css and images.

## templates
This folder consists of html templates used for web-pages.

## app.py
This is python file which consists of flask code. This needs to run to start our app.

## ml_backend.py
This file uses the trained model to predict the fault and localize it.



