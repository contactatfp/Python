**Introduction**

This code sample demonstrates the implementation of the k-Nearest Neighbors (KNN) algorithm for classification using Python. The KNN algorithm is a simple and effective approach for classification tasks. It works by finding the k-nearest data points for a given test data point and using them to predict the label for the test data point.

**Requirements**

To run this code, you will need to have the following libraries installed:

- pandas
- numpy
- matplotlib
- sklearn

**Usage**

The KNN algorithm is implemented in the **knn()** function, which takes in the following arguments:

- **test\_row** : A row of test data
- **train** : A pandas DataFrame containing the training data
- **num\_neighbors** : The number of nearest neighbors to consider for prediction

The function returns a list of the k-nearest neighbors for the given test data point.

**Example**

The code sample includes an example of using the KNN algorithm to classify data points in a 2D space. The data points are generated randomly and consist of two classes. The training and testing data are split using the **train\_test\_split()** function from scikit-learn. The KNN algorithm is then applied to the test data to make predictions, and the accuracy of the predictions is measured using the **accuracy\_score()** function from scikit-learn.

**References and sources**

- [GeeksforGeeks](https://www.geeksforgeeks.org/)
- [Real Python](https://realpython.com/)