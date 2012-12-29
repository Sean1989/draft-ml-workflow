# Circle equation: (x − xc)^2 + (y − yc)^2 = r^2
# (xc, yc) - center of the circle
# r - radius

# let the center be (0,0): x^2 + y^2 = r^2
# if we know x and r:   y = +/- sqrt(r^2 - x^2)
# =>
# generate x coords and then calculate y

new.points <- function(class = 0, radius = 5, distortion = 2, nr.of.samples = 100){
  # Returns a dataframe with points roughly located on a circle
  # Output:
  #    - dataframe:
  #         x | y | class
  #
  #      where (x, y) are coordinates of the points, all of the same pre-set "class".
  #
  set.seed(0)
  x <- sample(-radius:radius, nr.of.samples, replace=TRUE)
  y <- sqrt(radius^2 - x^2) * sample(c(-1,1), nr.of.samples, replace=TRUE) 
  # introduce distortion: our points should not be exactly on the circle
  x <- x + sample(-distortion:distortion, nr.of.samples, replace=TRUE)
  y <- y + sample(-distortion:distortion, nr.of.samples, replace=TRUE)
  # create a dataframe
  df <- data.frame(x = x, y = y, class = class)
  return(df)
}

##
## Working with data
##

df.first  <- new.points(class = 0, radius = 5, nr.of.samples = 100)
df.second <- new.points(class = 1, radius = 15, nr.of.samples = 120)

# create a plot
max <- 20
plot(-max:max, -max:max, type = "n", 
     main = "Points on two fuzzy circles",
     xlab = "Values of x", ylab = "Values of y")
points(df.first$x,  df.first$y,  pch = 5,  col = "tomato") # 5 for diamonds
points(df.second$x, df.second$y, pch = 19, col = "light blue")  # 19 for solid circles


# append the two datasets
dataset <- rbind(df.first, df.second)
# shuffle the data
dataset <- dataset[sample(nrow(dataset)),]

# output
write.csv(dataset, file="two_circles.csv", row.names=FALSE)