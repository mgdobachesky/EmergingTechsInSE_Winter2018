# Libraries
library(dplyr)
library(ggplot2)
library(scales)
library(reshape2)

# Load data
wine.df <- read.csv("wine.data", header=FALSE)
# Change column names of wine.df
names(wine.df) <- c("Type", 
                    "Alcohol", 
                    "Malic acid", 
                    "Ash", 
                    "Alcalinity of ash", 
                    "Magnesium", 
                    "Total phenois", 
                    "Flavnoids", 
                    "Nonflavanoid phenois", 
                    "Proanthocyanins", 
                    "Color intensity", 
                    "Hue", 
                    "OD280/OD315 of diluted wines", 
                    "Proline")

# Check and get rid of missing values
wine.df <- filter(wine.df, !is.na("Type"))
wine.df <- filter(wine.df, !is.na("Alcohol"))
wine.df <- filter(wine.df, !is.na("Malic acid"))
wine.df <- filter(wine.df, !is.na("Ash"))
wine.df <- filter(wine.df, !is.na("Alcalinity of ash"))
wine.df <- filter(wine.df, !is.na("Magnesium"))
wine.df <- filter(wine.df, !is.na("Total phenois"))
wine.df <- filter(wine.df, !is.na("Flavnoids"))
wine.df <- filter(wine.df, !is.na("Nonflavanoid phenois"))
wine.df <- filter(wine.df, !is.na("Proanthocyanins"))
wine.df <- filter(wine.df, !is.na("Color intensity"))
wine.df <- filter(wine.df, !is.na("Hue"))
wine.df <- filter(wine.df, !is.na("OD280/OD315 of diluted wines"))
wine.df <- filter(wine.df, !is.na("Proline"))

# Get dataset summary
summary(wine.df)

# Separate data by Type
wine.type1 <- filter(wine.df, Type == 1)
wine.type2 <- filter(wine.df, Type == 2)
wine.type3 <- filter(wine.df, Type == 3)

# Helper function to determine min value
determineMin <- function(type1, type2, type3) {
  min <- min(c(type1, type2, type3))
  min
}
# Helper function to determine max values
determineMax <- function(type1, type2, type3) {
  max <- max(c(type1, type2, type3))
  max
}

# Function to draw histograms
drawHist <- function(type1, type2, type3, name) {
  min = determineMin(type1, type2, type3)
  max = determineMax(type1, type2, type3)
  
  hist(type1, col=rgb(1,0,0,0.5), breaks=seq(min,max,l=10), xlim=c(min, max), ylim=c(0, 35), main=name, xlab=name)
  hist(type2, col=rgb(0,0,1,0.5), breaks=seq(min,max,l=10), xlim=c(min, max), ylim=c(0, 35), add=T)
  hist(type3, col=rgb(0,1,0,0.5), breaks=seq(min,max,l=10), xlim=c(min, max), ylim=c(0, 35), add=T)
  box()
  legend("topright", c("Type 1", "Type2", "Type3"), fill=c(rgb(1,0,0,0.5), rgb(0,0,1,0.5), rgb(0,1,0,0.5)))
}

# Alcohol
drawHist(wine.type1$Alcohol, wine.type2$Alcohol, wine.type3$Alcohol, 'Alcohol')

# Malic acid
drawHist(wine.type1$`Malic acid`, wine.type2$`Malic acid`, wine.type3$`Malic acid`, 'Malic acid')

# Ash
drawHist(wine.type1$Ash, wine.type2$Ash, wine.type3$Ash, 'Ash')

# Alcalinity of ash
drawHist(wine.type1$`Alcalinity of ash`, wine.type2$`Alcalinity of ash`, wine.type3$`Alcalinity of ash`, 'Alcalinity of ash')

# Magnesium
drawHist(wine.type1$Magnesium, wine.type2$Magnesium, wine.type3$Magnesium, 'Magnesium')

# Total phenois
drawHist(wine.type1$`Total phenois`, wine.type2$`Total phenois`, wine.type3$`Total phenois`, 'Total phenois')

# Flavnoids
drawHist(wine.type1$Flavnoids, wine.type2$Flavnoids, wine.type3$Flavnoids, 'Flavnoids')

# Nonflavanoid phenois
drawHist(wine.type1$`Nonflavanoid phenois`, wine.type2$`Nonflavanoid phenois`, wine.type3$`Nonflavanoid phenois`, 'Nonflavanoid phenois')

# Proanthocyanins
drawHist(wine.type1$Proanthocyanins, wine.type2$Proanthocyanins, wine.type3$Proanthocyanins, 'Proanthocyanins')

# Color intensity
drawHist(wine.type1$`Color intensity`, wine.type2$`Color intensity`, wine.type3$`Color intensity`, 'Color intensity')

# Hue
drawHist(wine.type1$Hue, wine.type2$Hue, wine.type3$Hue, 'Hue')

# OD280/OD315 of diluted wines
drawHist(wine.type1$`OD280/OD315 of diluted wines`, wine.type2$`OD280/OD315 of diluted wines`, wine.type3$`OD280/OD315 of diluted wines`, 'OD280/OD315 of diluted wines')

# Proline
drawHist(wine.type1$Proline, wine.type2$Proline, wine.type3$Proline, 'Proline')

