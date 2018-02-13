import numpy as np
import csv
from sklearn.linear_model import LogisticRegressionCV

# Bring in the X and y data
X = np.genfromtxt('train.x.csv', delimiter=',')
y = np.genfromtxt("train.y.csv", delimiter=',')

# Create cross-validation logistic regression with log loss evaluation metric
clf = LogisticRegressionCV(scoring='neg_log_loss')

# Fit the training data
clf.fit(X, y)

# Predict probabilities for the test cases
predicted_probabilities = clf.predict_proba(X)

# Write the predicted probabilities to a csv file
with open('predicted_probabilities.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for probability in predicted_probabilities:
        spamwriter.writerow(probability)
