# Circle equation: (x − xc)^2 + (y − yc)^2 = r^2
# (xc, yc) - center of the circle
# r - radius

# let the center be (0,0): x^2 + y^2 = r^2
# if we know x and r:   y = +/- sqrt(r^2 - x^2)
# =>
# generate x coords and then calculate y

r <- 5
r.second <- 15

nr.of.samples <- 100  
nr.of.samples.second <- 120

set.seed(0)
x <- sample(-r:r, nr.of.samples, replace=TRUE)
y <- sqrt(r^2 - x^2) * sample(c(-1,1), nr.of.samples, replace=TRUE) # so we can have negative y's as well
# introduce fuzziness
x <- x + sample(-2:2, nr.of.samples, replace=TRUE)
y <- y + sample(-2:2, nr.of.samples, replace=TRUE)

set.seed(0)
x.second <- sample(-r.second:r.second, nr.of.samples.second, replace=TRUE)
y.second <- sqrt(r.second^2 - x.second^2) * sample(c(-1,1), nr.of.samples.second, replace=TRUE) # so we can have negative y's a well
# introduce fuzziness
x.second <- x.second + sample(-2:2, nr.of.samples.second, replace=TRUE)
y.second <- y.second + sample(-2:2, nr.of.samples.second, replace=TRUE)

# create a plot
max <- r.second + 5
plot(-max:max, -max:max, type = "n", 
     main = "Points on two fuzzy circles",
     xlab = "Values of x", ylab = "Values of y")
points(x,y, pch = 5, col = "tomato") # 5 for diamonds
points(x.second, y.second, pch = 19, col = "light blue")  # 19 for solid circles