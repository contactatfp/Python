### SVM and PCA

This code sample is a solution for classifying cancer type based on gene expression data using support vector machines and principal component analysis (PCA).

### Prerequisites

- Python 3
- NumPy
- Pandas
- scikit-learn
- Matplotlib
- Seaborn

### Installing

1. Clone or download the repository
2. Install the required libraries using pip or your preferred method

matplotlib seaborn

### Running the code

1. Mount Google Drive by running the **drive.mount** cell
2. Run the remaining cells in the notebook to load the data, perform PCA, train and evaluate the support vector machine (SVM) model, and visualize the results

### Usage

The code loads the necessary libraries and sets the random number generator seed. It then loads the data from a CSV file in Google Drive and extracts the numeric columns as the input variables and the **Class** column as the target variable.

Next, the code performs PCA to reduce the dimensionality of the input data and selects the top two principal components for visualization. It then splits the data into training and testing sets and standardizes the input variables using **StandardScaler**.

The code then trains and evaluates an SVM model using a linear kernel and a radial basis function (RBF) kernel, respectively. It uses **GridSearchCV** to tune the hyperparameters of the SVM models and selects the best models based on their performance on the training data.

Finally, the code evaluates the performance of the two models on the testing data using metrics such as accuracy, precision, and recall, and plots the confusion matrix to visualize the results.

### Data

The data for this code sample consists of gene expression data from various types of cancer, including breast, bladder, colon, glioblastoma, head and neck, kidney, liver, lung, ovarian, and prostate cancer. The input variables are gene expression levels, and the target variable is the type of cancer. The data has been preprocessed to remove missing values and outliers.