# Returns a dataframe with points roughly located on a circle

# Input:
#    - class: set the class here, it will be the same for all generated points. This value is only used to generate the "class" column in the resulting dataframe.
#    - radius: the radius of the circle
#    - distortion: how far away our points can go from the circle?
#    - nr.of.samples: number of samples to generate

# Output:
#    - dataframe:
#         x | y | class
#
#      where (x, y) are coordinates of the points, 
#      all points are of the same pre-set "class".

new.points <- function(class = 0, radius = 5, distortion = 2, nr.of.samples = 100){

    
  # Circle equation with the center in (0,0): x^2 + y^2 = radius^2
  # if we know x and radius:   y = +/- sqrt(radius^2 - x^2)  
  set.seed(0)
  x <- sample(-radius:radius, nr.of.samples, replace=TRUE)
  y <- sqrt(radius^2 - x^2) * sample(c(-1,1), nr.of.samples, replace=TRUE) 
  
  # Introduce distortion: our points should not be exactly on the circle
  x <- x + sample(-distortion:distortion, nr.of.samples, replace=TRUE)
  y <- y + sample(-distortion:distortion, nr.of.samples, replace=TRUE)
  
  # Create the dataframe
  df <- data.frame(x = x, y = y, class = class)
  return(df)
}
