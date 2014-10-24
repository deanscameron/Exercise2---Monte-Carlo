""" Monte-Carlo functions file: 
    1) Compute energy at current density
    2) Move randomly chosen partical left or right
    3) Compute second energy
    4) Compare the energies
       i) Accept move if second energy is lower
	   ii) Otherwise compute P_0=e^{-\frac{E_1-E_0}{T}} and P_1 (a random number
	       accept move only if P_0 > P_1
    5) Repeat
"""

# energy()
# Use the same energy function as from the Classroom Exercise


# move_random()
# Function that selects a random particle
# Randomly moves that particle left or right


# comparison()
# Function that runs the comparisons
# Must compare the energies at both densities
# Must return a density as per the criteria in 4)


# monte_carlo()
# Function that repeats move_random and comparisons a given number of times
# Must also depend on the initial density and temperature