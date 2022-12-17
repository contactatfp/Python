### Regression

This code sample is a solution for predicting the compressive strength of concrete using data from [Kaggle](https://www.kaggle.com/). It uses regression models to fit a function to the data and make predictions about the compressive strength of concrete based on the input variables.

The code first trains and evaluates a linear regression model, which assumes that the relationship between the input variables and the target variable is linear. It then trains and evaluates a polynomial regression model, which can capture nonlinear relationships between the variables by adding polynomial terms to the model. The performance of the two models is compared using metrics such as mean squared error and R^2 score.

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

### Running the code

1. Mount Google Drive by running the **drive.mount** cell
2. Run the remaining cells in the notebook to load the data, visualize the relationships between variables, and build and evaluate the model

### Usage

The code loads the necessary libraries and sets the random number generator seed. It then loads the data from a CSV file in Google Drive and performs some basic visualization to understand the relationships between the variables.

Next, the code defines a function **diagnostic\_plots** that creates scatterplots to visualize the relationship between a given variable and the target variable (compressive strength). The function is then called for each variable in the dataset.

The code then calculates the correlations between variables and plots the top 9 correlations with the target variable.

Finally, the code prepares the data for modeling by scaling the input variables and splitting the data into training and testing sets. It then trains and evaluates a linear regression model and a polynomial regression model using the training data, and compares the performance of the two models on the testing data using metrics such as mean squared error and R^2 score.

### Data

The data for this code sample comes from [Kaggle](https://www.kaggle.com/). It consists of 1030 records of concrete compressive strength, along with the following variables:

- cement
- slag
- flyash
- water
- superplasticizer
- coarseaggregate
- fineaggregate
- age

The target variable is the compressive strength of the concrete, measured in megapascals (MPa).