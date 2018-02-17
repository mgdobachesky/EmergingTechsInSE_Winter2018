import numpy as np
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import confusion_matrix
from sklearn.calibration import CalibratedClassifierCV
from sklearn.naive_bayes import GaussianNB

# Bring in the wine data
wine_data = np.genfromtxt('wine.data', delimiter=',')

# Shuffle the data before working with it
np.random.shuffle(wine_data)

# Get the total number of rows in the wine data set
n_samples = wine_data.shape[0]

# Get the total number of columns in the wine data set
n_cols = wine_data.shape[1]

# Get the numbers to use when splitting the dataset
n_train = int(0.7 * n_samples)

# Separate the dataset into training, validation, and testing datasets
wine_train = wine_data[:n_train, :]
wine_test = wine_data[n_train:, :]

# Separate the datasets on X and y values
wine_train_X = wine_train[:, 1:]
wine_train_y = wine_train[:, :1]
wine_test_X = wine_test[:, 1:]
wine_test_y = wine_test[:, :1]


# Function for running logistic regression
def run_logistic_regression():
    print("~ Logistic Regression ~")

    # Create Logistic Regression
    # with c value under consideration
    # with cross-validation folds under consideration
    # and evaluation metric of log loss
    model = LogisticRegressionCV(Cs=10,
                                 cv=10,
                                 scoring='neg_log_loss')

    # Fit the model
    model.fit(wine_train_X, wine_train_y.ravel())

    # Predict y with test data
    predict_y = model.predict(wine_test_X)

    # Find the accuracy score
    accuracy = model.score(wine_test_X, wine_test_y)

    # Create a confusion matrix
    cm = confusion_matrix(wine_test_y, predict_y)

    # Print findings
    print("Accuracy: ", accuracy)
    print("Confusion Matix:")
    print(cm)


def run_sigmoid():
    print("~ Calibrated Classifier ~")

    # Create sigmoid
    model = CalibratedClassifierCV(GaussianNB(),
                                   method='sigmoid',
                                   cv=10)

    # Fit the model
    model.fit(wine_train_X, wine_train_y.ravel())

    # Predict y with test data
    predict_y = model.predict(wine_test_X)

    # Find the accuracy score
    accuracy = model.score(wine_test_X, wine_test_y)

    # Create a confusion matrix
    cm = confusion_matrix(wine_test_y, predict_y)

    # Print findings
    print("Accuracy: ", accuracy)
    print("Confusion Matix:")
    print(cm)


# Run logistic regression
run_logistic_regression()

print()

# Run Sigmoid
run_sigmoid()

