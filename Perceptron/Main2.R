# Get working directory
getwd()

# Set working directory if needed
#setwd("C:/Users/Indrani/Desktop/SE 428/Assignments/HW 3")

# Read the data
data <- read.csv("dataset.csv")

# Source and run Perceptron
source("Perceptron.r")
perceptron.model <- perceptron(data)
perceptron.model(c(2,2))

