
# Perceptron calculates the decision surface depending on the 
# weights of the feature vectors

perceptron <- function (data){
data.matrix <- as.matrix(data)

df <- subset(data, select = x1: x2)
mat <- as.matrix(df)

# learner rate
n <- 0.3
b <- 0

# initial w
w <- c(0,0)

# maximum radius of the furthest vector
norm <- mat^2
row.sum <- max(rowSums(norm, na.rm = FALSE, dims = 1))
r <- sqrt(row.sum)

data.matrix[4, ncol(data.matrix)]
sign(w %*% mat[4,] - b)
     
# the perceptron algorithm 
repeat{
  failed <- FALSE
  for (i in 1: nrow(data.matrix)){
    yi <- data.matrix[i, ncol(data.matrix)]
     if (sign(w %*% mat[i,] - b) != yi){
	 
       # calculate the w,b values
       w <- w + n * mat[i,] * yi
       b <- b - n * yi * r^2
       
       print(b)
     }
  }
  
  for (i in 1: nrow(data.matrix)){
    print((sign(w %*% mat[i,] - b)))
    
	# check if the signs match
    if (sign(w %*% mat[i,] - b) != data.matrix[i, ncol(data.matrix)]){
      failed <- TRUE
    }
  }
  # if all signs pass, learning is complete
  if(!failed)
    break
  
}

# the decision surface is perpendicular to w
slope <- -w[1]/w[2]  # d = w = (w1, w2), slope of w = w[2]/w[1]
intercept <- b/w[2]

# Seperate the positive data points from the negative ones
pos <- data[which(data[,3]>0), -3]

# Plot the data points
plot(data$x1, data$x2, col = "green", pch = 19, xlab = "X1", ylab = "X2")

# Add the positive points back to the plot
points(pos$x1, pos$x2, col="blue", pch=19)

# Draw the decision surface
abline(intercept, slope, col = "red" )


# perceptron prediction function
  function(x){
     val <- (w %*%x - b)
     sign(val)
  }
}


