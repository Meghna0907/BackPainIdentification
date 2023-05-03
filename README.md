# BackPainIdentification
This project aims to find the cause of lower back pain by identifying whether the patient has normal spine or abnormal.

OBJECTIVE
To predict the spinal abnormality based on collected physical spine data by using supervised 
machine learning approaches such as K-Nearest Neighbors (KNN), Random Forest Classifier, 
Logistic Regression, Support Vector Machine(SVM), Decision Trees on physical spine dataset 
and using the best fit model to aid the process of detection of abnormality in lower spine.

METHODOLOGY
• Data Collection
Lower Back Pain Symptoms Dataset Collection of Physical Spine data (from Kaggle) has 
been analyzed in this project. The data consists of 13 attributes with 12 numeric 
predictors and 1 binary class attribute namely pelvic_incidence, pelvic_tilt, 
lumbar_lordosis_angle, sacral_slope, pelvic_radius, degree_spondylolisthesis, 
pelvic_slope, Direct_tilt, thoracic_slope, cervical_tilt, sacrum_angle, scoliosis_slope, and 
target. 
Dataset Source: https://www.kaggle.com/sammy123/lower-back-pain-symptoms-dataset/version/1
• Data Preprocessing
The data is used to predict the abnormality of spine, using the independent variables, as 
normal or abnormal. The whole data contained 210 abnormal and 100 normal instances. 
The data did not contain any null values already. The correlation between features were 
studied using correlation matrix, emphasizing the dependency of target variable on the 
feature, degree_spondylolisthesis, the most. Further the data was checked for normal 
distribution and was standardized using Standard Scaler. The data was then divided into 
training and test dataset as 80% and 20% respectively.
• Classification
Use of supervised machine learning algorithms has been done this study. A comparative 
study of five different algorithms was done to determine which algorithm works best to 
predict the given problem. The algorithms used were as follows: Logistic Regression, 
Random Forest Classifier, K Nearest Neighbor, Decision Tree, Support Vector Machine.
• Training and Testing
The data was divided into test data and train data as 20% and 80% respectively. The 
models were trained on the training data. The models were then tested on test data and 
were cross-validated.

<img src="https://user-images.githubusercontent.com/84454062/235827751-14f208b5-2bb0-48f1-9a2f-6268b5e0d1b7.png" width="60" height="40">

Hyperparameter Tuning

<img src="https://user-images.githubusercontent.com/84454062/235827910-22679476-1f2b-4a3a-87f3-21c26adca3f5.png" width="60" height="40">

Classification Report

<img src="https://user-images.githubusercontent.com/84454062/235828042-768fe9f3-456a-48e3-bda2-d0799316653d.png" width="60" height="40">

Confusion Matrix
<img src="https://user-images.githubusercontent.com/84454062/235827992-0f10f90c-f373-4dd2-b157-555bb7ba4d96.png" width="50" height="40">

CONCLUSION 
It can be concluded by using Random Forest Classifier algorithm and hyper-parameter 
optimization (max_depth, min_samples_leaf, min_samples_split, n_estimators), an 
accuracy of 87% can be achieved to identify the abnormality of Lower Back Pain with 
Kaggle Dataset.
Further, this data can be tested using other techniques like neural networks.


