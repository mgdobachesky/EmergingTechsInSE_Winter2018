import numpy as np
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, make_scorer

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

# Layout confusion matrix scoring architecture
def tp(y_true, y_pred): return confusion_matrix(y_true, y_pred)[0, 0]
def tn(y_true, y_pred): return confusion_matrix(y_true, y_pred)[1, 1]
def fp(y_true, y_pred): return confusion_matrix(y_true, y_pred)[1, 0]
def fn(y_true, y_pred): return confusion_matrix(y_true, y_pred)[0, 1]


# Create confusion matrix scoring
scoring = {'tp': make_scorer(tp), 'tn': make_scorer(tn),
           'fp': make_scorer(fp), 'fn': make_scorer(fn)}

# Create a classifier using a grid search
# with Support Vector Classification over defined parameters
clf = GridSearchCV(svc, parameters, cv=3, verbose=True, scoring=scoring, refit=False)

# Fit the data
clf.fit(bcw_train_X, bcw_train_y.ravel())

# Create a place to store two best models
two_best_models = [(0, 0, 0), (0, 0, 0)]

# Find two best models
for index in enumerate(clf.cv_results_['params']):
    # Get correct and incorrect predictions
    tp = int(clf.cv_results_['mean_test_tp'][index[0]])
    tn = int(clf.cv_results_['mean_test_tn'][index[0]])
    fp = int(clf.cv_results_['mean_test_fp'][index[0]])
    fn = int(clf.cv_results_['mean_test_fn'][index[0]])

    # Get values to use in calculating confusion matrix's score
    total_records = tp + tn + fp + fn
    correct_predictions = tp + tn

    # Calculate confusion matrix and its score
    cm = [[tp, fn], [fp, tn]]
    score = correct_predictions/total_records

    # If the previous highest score is less than the score of the current model
    if score > two_best_models[0][0]:
        two_best_models[0] = (score, clf.cv_results_['params'][index[0]], cm)
    # Else if the previous second highest score is less than the score of the current model and the kernel is different
    elif score > two_best_models[1][0] and clf.cv_results_['params'][index[0]]['kernel'] != two_best_models[0][1]['kernel']:
        two_best_models[1] = (score, clf.cv_results_['params'][index[0]], cm)


# Print out the results
print()
print('Best Model Score:', two_best_models[0][0])
print('Best Model Params:', two_best_models[0][1])
print('Best Model Confusion Matrix:', two_best_models[0][2])
print()
print('Second Best Model Score', two_best_models[1][0])
print('Second Best Model Params:', two_best_models[1][1])
print('Second Best Model Confusion Matrix:', two_best_models[1][2])
print()
