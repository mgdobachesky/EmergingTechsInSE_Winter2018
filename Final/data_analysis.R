# Libraries
library(dplyr)
library(ggplot2)
library(scales)
library(reshape2)

# Load data
bcw.df <- read.csv("bcw.data", header=FALSE)
# Change column names of bcw.df
names(bcw.df) <- c("SCN", 
                    "CTH", 
                    "UCZ", 
                    "UCS", 
                    "MAD", 
                    "SEC", 
                    "BNC", 
                    "BCH", 
                    "NNC", 
                    "MTS", 
                    "Class")

# Check and get rid of missing values
bcw.df <- filter(bcw.df, !is.na("SCN"))
bcw.df <- filter(bcw.df, !is.na("CTH"))
bcw.df <- filter(bcw.df, !is.na("UCZ"))
bcw.df <- filter(bcw.df, !is.na("UCS"))
bcw.df <- filter(bcw.df, !is.na("MAD"))
bcw.df <- filter(bcw.df, !is.na("SEC"))
bcw.df <- filter(bcw.df, !is.na("BNC"))
bcw.df <- filter(bcw.df, !is.na("BCH"))
bcw.df <- filter(bcw.df, !is.na("NNC"))
bcw.df <- filter(bcw.df, !is.na("MTS"))
bcw.df <- filter(bcw.df, !is.na("Class"))

# Get dataset summary
summary(bcw.df)

# Separate data by Type
bcw.type1 <- filter(bcw.df, Class == 2)
bcw.type2 <- filter(bcw.df, Class == 4)

# Helper function to determine min value
determineMin <- function(type1, type2) {
  min <- min(c(type1, type2))
  min
}
# Helper function to determine max values
determineMax <- function(type1, type2) {
  max <- max(c(type1, type2))
  max
}
# Helper function to determine the max value for y
determineYLim <- function(type1, type2) {
  maxRows <- max(c(table(type1), table(type2)))
  maxRows = maxRows * 1.1
  maxRows
}

# Function to draw histograms
drawHist <- function(type1, type2, name) {
  min = determineMin(type1, type2)
  max = determineMax(type1, type2)
  maxRows = determineYLim(type1, type2)
  
  hist(type1, col=rgb(0,1,0,0.5), breaks=seq(0,max,l=10), xlim=c(0, max), ylim=c(0, maxRows), main=name, xlab=name)
  hist(type2, col=rgb(1,0,0,0.5), breaks=seq(0,max,l=10), xlim=c(0, max), ylim=c(0, maxRows), add=T)
  box()
  legend("topright", c("Benign", "Malignant"), fill=c(rgb(0,1,0,0.5), rgb(1,0,0,0.5)))
}

# CTH 
drawHist(bcw.type1$CTH, bcw.type2$CTH, 'Clump Thickness')

# UCZ
drawHist(bcw.type1$UCZ, bcw.type2$UCZ, 'Uniformity of Cell Size')

# UCS
drawHist(bcw.type1$UCS, bcw.type2$UCS, 'Uniformity of Cell Shape')

# MAD 
drawHist(bcw.type1$MAD, bcw.type2$MAD, 'Marginal Adhesion')

# SEC 
drawHist(bcw.type1$SEC, bcw.type2$SEC, 'Single Epithelial Cell Size')

# BNC 
drawHist(bcw.type1$BNC, bcw.type2$BNC, 'Bare Nuclei')

# BCH 
drawHist(bcw.type1$BCH, bcw.type2$BCH, 'Bland Chromatin')

# NNC
drawHist(bcw.type1$NNC, bcw.type2$NNC, 'Normal Nucleoli')

# MTS 
drawHist(bcw.type1$MTS, bcw.type2$MTS, 'Mitoses')

# Class
drawHist(bcw.type1$Class, bcw.type2$Class, 'Class')
