import numpy as np
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix


# Bring in data
bcw_data = np.genfromtxt('bcw.data', delimiter=',')

# Shuffle data
np.random.shuffle(bcw_data)

# Get dataset metadata
n_rows = bcw_data.shape[0]
n_cols = bcw_data.shape[1] - 1

# Define percentage to split data on
n_train = int(0.7 * n_rows)

# Separate the dataset
# NOTE: First column is an ID number and is therefore not needed
bcw_train = bcw_data[:n_train, 1:]
bcw_test = bcw_data[n_train:, 1:]

# Separate the training data on X and y values
bcw_train_X = bcw_train[:, :n_cols-1]
bcw_train_y = bcw_train[:, n_cols-1:]

# Separate the testing data on X and y values
bcw_test_X = bcw_test[:, :n_cols-1]
bcw_test_y = bcw_test[:, n_cols-1:]


# Create SVM object
svc = svm.SVC()

# Define parameters to test the grid search with
parameters = {
    'kernel': ('linear', 'poly', 'rbf', 'sigmoid'),
    'C': [.01, .1, 1, 10],
    'degree': [2, 3, 4, 5],
    'gamma': [.01, .1, 1, 10],
    'coef0': [x for x in range(-10, 30, 10)]
}

# Create a classifier using a grid search
# with Support Vector Classification over defined parameters
clf = GridSearchCV(svc, parameters, cv=3, verbose=True)

# Fit the data
clf.fit(bcw_train_X, bcw_train_y.ravel())

# Get the score for the best fit model
score = clf.score(bcw_test_X, bcw_test_y)

# Predict the target values using the best model
predict_y = clf.predict(bcw_test_X)

# Create a confusion matrix using the best model's prediction
cm = confusion_matrix(bcw_test_y, predict_y)

# Print out the results
print()
print('Best Model:', clf.best_params_)
print()
print('Score:', clf.best_score_)
print()
print('Confusion Matrix:')
print(cm)
