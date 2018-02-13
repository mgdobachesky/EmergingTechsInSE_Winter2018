from sklearn.neighbors import KNeighborsClassifier

# In this program we construct a NeighborsClassifier class from the training
# data(array) and ask who’s the closest point  to the test data points
# The data set
x = [[0, 0], [0.5, 0], [1, 1], [0.5, 1], [0.5, 0.5], [1, 0], [0, 1]]
y = [+1, +1, +1, +1, -1, -1, -1]

neigh1 = KNeighborsClassifier(1)
neigh3 = KNeighborsClassifier(3)
neigh5 = KNeighborsClassifier(5)

# Fit the models
neigh1.fit(x, y)
neigh3.fit(x, y)
neigh5.fit(x, y)

# Enter the test data point
test_data = [[0.2, 0.2], [0.2, 0.8], [0.8, 0.8], [1, 1], [1, 0]]

# Now use the model ‘neigh’ to classify your test data
print("~ Classified Data ~")
print("One Nearest Neighbor: ", neigh1.predict(test_data))
print("Three Nearest Neighbors: ", neigh3.predict(test_data))
print("Five Nearest Neighbors: ", neigh5.predict(test_data))

# Print the neighbors
print("\n~ Each point's distance from one neighbor: ~\n", neigh1.kneighbors(test_data))
print("\n~ Each point's distance from three neighbors: ~\n", neigh3.kneighbors(test_data))
print("\n~ Each point's distance from five neighbors: ~\n", neigh5.kneighbors(test_data))

