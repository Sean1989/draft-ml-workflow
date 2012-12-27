# Circle equation: (x − xc)^2 + (y − yc)^2 = r^2
# (xc, yc) - center of the circle
# r - radius

# let the center be (0,0): x^2 + y^2 = r^2
# if we know x and r:   y = +/- sqrt(r^2 - x^2)
# =>
# generate x coords and then calculate y

r <- 5

set.seed(0)
x <- sample(-r:r, 100, replace=TRUE)
y <- sqrt(r^2 - x^2) * sample(c(-1,1), 100, replace=TRUE) # so we can have negative y's as well
plot(x, y)

r.second <- 10
set.seed(0)
x.second <- sample(-r.second:r.second, 100, replace=TRUE)
y.second <- sqrt(r.second^2 - x.second^2) * sample(c(-1,1), 100, replace=TRUE) # so we can have negative y's as well
lines(x.second, y.second)

# create a plot
plot(-15:15, -15:15, type = "n", 
     main = "Points on two concentric circles",
     xlab = "Values of x", ylab = "Values of y")
points(x,y, pch = 5, col = "tomato") # 5 for diamonds
points(x.second, y.second, pch = 19, col = "light blue")  # 19 for solid circles

