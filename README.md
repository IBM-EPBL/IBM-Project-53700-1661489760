Web Phishing Detection🕵️‍♀️
===========================

Category: Machine Learning
==========================

![N\|Solid](https://images.pexels.com/photos/459653/pexels-photo-459653.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)
\# Objective A phishing website is a common social engineering method
that mimics trustful uniform resource locators (URLs) and webpages. The
objective of this project is to train machine learning models on the
dataset given to predict phishing websites. Both phishing and benign
URLs of websites are gathered to form a dataset and from them required
URL and website content-based features are extracted. The performance
level of each model is measured and compared.

Data Collection and Analysis
============================

The given data
(https://github.com/IBM-EPBL/IBM-Project-38311-1660377839/blob/main/final%20deliverables/data/dataset\_website.csv)
contains both phishing and benign URLs of websites with various website
content-based features.

The above mentioned dataset is uploaded to the 'final deliverables/data'
folder of this repository.

From data distribution graph and correlation matrix, we can conclude
that the 16 of the given features do not have much impact on the result.
So they are removed from further processing. The final set of features
that are used to build the model are shown in the figure below.

![N\|Solid](https://user-images.githubusercontent.com/64459672/199578614-f8cb7f81-9da0-43a8-b6eb-5381970a9768.png)

Models & Training
=================

Before stating the ML model training, the data is split into 80-20 i.e.,
8844 training samples & 2211 testing samples. From the dataset, it is
clear that this is a supervised machine learning task. There are two
major types of supervised machine learning problems, called
classification and regression. This data set comes under classification
problem, as the input URL is classified as phishing (1) or legitimate
(0). The supervised machine learning models (classification) considered
to train the dataset in this project are:

Decision Tree Random Forest XGBoost Support Vector Machines All these
models are trained on the dataset and evaluation of the model is done
with the test dataset. The elaborate details of the models & its
training are mentioned in

End Results
===========

From the obtained results of the above models, XGBoost Classifier has
highest model performance of 92.3%. So the model is saved to the file
XGBoostClassifier.pickle.dat.

Team Members
============

Keerthika

Sivapriya

Alwin mercily

Subasri

Anusha

Team ID: PNT2022TMID46905
