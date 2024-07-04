<p align="center">
 <h1 align="center">Predicting the Genre of Vietnamese Articles</h1>
</p>

## Introduction

Hello, this is a project on predicting the genres of articles in Vietnam by collecting data from what is considered one of the largest and most famous online newspapers in Vietnam, "**vnexpress.net**". After the data is cleaned and features are extracted, it is trained through 9 machine learning models, fine-tuning each hyperparameter to select the optimal model that best suits the problem at hand. Finally, the user's predictions are visualized through a simple web application. 

## Dataset
The dataset consists of **2324** articles spanning various fields: travel, health, business, sports, etc. The data is divided into 6 attributes: title, abstract, content, author, date, and label. You can find the data in .csv format in the directory **./data/vnexpress_data.csv.**

## Categories:
The table below lists all the article genres that I have utilized:
|               |                    |               |                |
|---------------|:------------------:|:-------------:|:--------------:|
|   real_estate |   law              |   travel      |   sports       |
|   education   |   current_affairs  |   health      | digitalization |
|   world       |       vehicles     |  business     |                |
|    science    |   perspective      | entertainment |                |

## Trained models

Utilizing 9 Machine Learning Models Currently Considered Most Suitable for the Problem: **LogisticRegression, MultinomialNB, BaggingClassifier, DecisionTreeClassifier, LinearSVC, SGDClassifier, KNeighborsClassifier, RandomForestClassifier, GradientBoostingClassifier.**

## Training

The training data is split at a ratio of **8 : 2**, with feature extraction performed using **TFIDF**. Below are the results of each model's predictions based on both the training and test sets:

<img src="demo/output1.png" width="800"> 

**Finally**, here are the results of the 2 standout models after hyperparameter optimization:

<img src="demo/output2.png" width="800"> 

## APP

Visualize the predictions by building a simple web app using **Flask**. You can try out the app by running the **app.py** file or by visiting the link **lethanhhiep.pythonanywhere.com**(expired) to experience it!

<img src="demo/app.png" width="800"> 

## Requirements

* **python 3.10**
* **scikit-learn**
* **pandas**
* **underthesea**
* **flask 3.0**
