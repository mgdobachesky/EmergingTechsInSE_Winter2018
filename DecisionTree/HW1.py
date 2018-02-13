import numpy as np
from sklearn import tree
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

# This program will create a model using decision tree learning algorithm


# read the data from the downloaded text file
data = np.genfromtxt("Data.txt",delimiter=",")

# shuffle the training data
np.random.shuffle(data)

# Find out total number of rows in the data file = total number of data
n_samples = data.shape[0]

# Number of columns = attributes/featues
n_cols = data.shape[1]

# We only wan to use 70% as training data
n_train = (int)(0.7*n_samples) # number of training data

# Separate the train data
train = data[ :n_train, : ]

# Separate the test data attributes/features from the target(first col in this dataset)
test_data = data[n_train:, 1:]
target_data = data[n_train:, :1] # the last column is the target

#Create the list to store the results: 10 lists of 10 runs each = 100 values
result_list = []

# Vary Training data size: 10%, 20%, 30%, 40%.... 90%, 100%
for j in range(10, 110, 10):

    # Accuracy list will hold the model accuracies for the next 10 runs
    accuracy_list = []

    for i in range(1,11):

        # Shuffle the data each time
        np.random.shuffle(train)

        #Vary the number of training data size
        current_n_train = (int)((j/100)*train.shape[0])

        #Current training data used for fitting the model
        train_data= train[ :current_n_train, 1:]

        #Separate training target from the training data and
        # use it to fit the model
        training_target = train[ :current_n_train , : 1]

        # generate the tree and save it under the name clf
        clf = tree.DecisionTreeClassifier()

        # fit the model by training with train data and target data and
        # save model(clf) again
        clf = clf.fit(train_data, training_target)

        # predict the labels using model and test data,
        # save it under the name prediction
        prediction = clf.predict(test_data)

        # Confusion matrix
        cm = confusion_matrix(target_data, prediction)

        # measure Accuracy of your model with different training data
        t = sum(sum(l) for l in cm)
        accuracy = sum(cm[i][i] for i in range(len(cm))) / t

        # Append the accuracy calculated to our accuracy list
        accuracy_list.append(accuracy)

    # Append the accuracy list(10 values in the each list) to our result list
    result_list.append(accuracy_list)

# Create the boxplot
plt.boxplot(result_list)

# Show the box plot
plt.show()

# generate the tree.dot file to visualize the graph
tree.export_graphviz(clf, out_file= 'tree.dot')

# find the tree.dot file under your working folder on the left)
# Copy the code at http://webgraphviz.com/ to generate your tree