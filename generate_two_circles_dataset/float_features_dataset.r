# Returns a dataframe with points roughly located on a circle. 
new.points <- function(class = 0, radius = 5, distortion = 2, nr.of.samples = 100){      
  set.seed(0)
  x <- sample(-radius:radius, nr.of.samples, replace=TRUE)
  y <- sqrt(radius^2 - x^2) * sample(c(-1,1), nr.of.samples, replace=TRUE)   
  x <- x + sample(-distortion:distortion, nr.of.samples, replace=TRUE) + 0.01
  y <- y + sample(-distortion:distortion, nr.of.samples, replace=TRUE)  
  df <- data.frame(x = x, y = y, result = class)
  return(df)
}

##
## Working with data
##

# generate points of two different classes
df.first  <- new.points(class = 0, radius = 5, nr.of.samples = 100)
df.second <- new.points(class = 1, radius = 15, nr.of.samples = 120)

# create a plot
max <- 20
plot(-max:max, -max:max, type = "n", 
     main = "Points on two fuzzy circles",
     xlab = "Values of x", ylab = "Values of y")
points(df.first$x,  df.first$y,  pch = 5,  col = "tomato") # 5 for diamonds
points(df.second$x, df.second$y, pch = 19, col = "light blue")  # 19 for solid circles


# append the two dataframes
dataset <- rbind(df.first, df.second)
# shuffle the data
dataset <- dataset[sample(nrow(dataset)),]

# output
write.csv(dataset, file="../data/float_features_dataset.csv", row.names=FALSE)
