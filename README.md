# Breast-cancer-detection

* An application for breast cancer detection. The app can tell whether the breast mass is benign(non-cancerous cells) or malignant(cancerous cells).
* is a Python3 project to classify cancer data using Google's TensorFlow library and Neural Networks. The goal of this project was to validate and demonstrate that modern machine learning techniques in neural nets could prove to be useful in classifying cancer datasets.
* Link of the dataset used: http://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29 and http://portals.broadinstitute.org/cgi-bin/cancer/datasets.cgi
* This repo contains two main sections:

  -  dnn_data_classifier - A Deep Neural Network implementation to classify breast cancer tumours as benign or malignant depending on measurements taken directly from tumours.
  -  cnn_image_classifier - A Convolutional Neural Network implementation to classify breast tumours as benign or malignant using images of histology slides.

* The attributes in the sample are in the range (1-10). So, doctors will enter the values of attributes and clicking on the compute button can tell whether it's benign or malignant.
* Video : (will be available soon)  

### Requirements ###

* Python >=2.7.14
* TensorFlow >= 1.0.0
* Flask
* Heroku
