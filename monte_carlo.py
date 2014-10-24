"""File used to run the Monte-Carlo"""

# contains inputs for the functions

# set the initial density
density = [2, 2, 2, 2, 2]

# set the initial temperature
temperature = 100

# set the number of iterations
iterations = 10

from monte_carlo_functions import monte_carlo

monte_carlo(density, iterations, temperature)
