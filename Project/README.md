# **README**

This code demonstrates how to preprocess and classify the stroke data using Support Vector Machines (SVMs). The data is first encoded and then split into training and testing sets. The hyperparameters of the SVM model are optimized using a grid search and cross-validation. The performance of the model is then evaluated using various metrics, including accuracy, precision, recall, f1 score, and ROC AUC. The code also includes visualization of the confusion matrix and a classification report.

**Dependencies**

- numpy
- pandas
- sklearn
- matplotlib
- seaborn
- imblearn
- yellowbrick

**Usage**

1. Load the necessary libraries and mount the Google Drive where the data is stored:
2. Load the data and perform one-hot encoding on the categorical features:
3. Split the data into training and testing sets and oversample the training set using SMOTE.
4. Standardize the data and create an SVM model with a linear kernel.
5. Use a grid search and cross-validation to find the optimal hyperparameters for the model.