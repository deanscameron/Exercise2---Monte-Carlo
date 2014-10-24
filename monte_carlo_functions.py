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


def energy(density, coefficient=1):
	# Energy from classroom exercise
	# Could be replaced with any energy function
 
	from numpy import array, any, sum

	density = array(density)

	# If length non-zero then type must be integers
	if density.dtype.kind != 'i' and len(density) > 0:
		raise TypeError("Density should be an array of integers.")
	# Entries must be non-negative
	if any(density < 0):
		raise ValueError("Density should be an array of positive integers.")
	# Denisty must be a 1-D array 
	if density.ndim != 1:
		raise ValueError("Density should be an a 1-D array.")
  
	return coefficient * 0.5 * sum(density * (density - 1))


def move_random(density):	
	import random 
	
	# rand_particle chooses the random particle in density
	rand_particle = random.randint(0, (len(density)-1))
	
	# direction chooses the direction the particle moves
	# direction = 0, then move left
	# direction = 1, then move right
	direction = random.randint(0,1)
		
	if density[rand_particle] <= 0:
		# if there are no particles in the selected position then do nothing to the array
		density[rand_particle] = (density[(rand_particle)])
	
	elif rand_particle <= 0:
		# if the particle selected is in the left most element it has to move right
		density[rand_particle] = (density[(rand_particle)]-1)
		density[(rand_particle + 1)] = (density[(rand_particle + 1)] + 1)
	
	elif rand_particle >= (len(density)-1):
		# if the particle selected is in the right most element it has to move left
		density[rand_particle] = (density[(rand_particle)]-1)
		density[(rand_particle - 1)] = (density[(rand_particle - 1)] + 1)
	
	elif direction <= 0:
		# otherwise the particle moves left for direction 0
		density[rand_particle] = (density[(rand_particle)]-1)
		density[(rand_particle - 1)] = (density[(rand_particle - 1)] + 1)
	
	else:
		# and the particle moves right for direction 1
		density[rand_particle] = (density[(rand_particle)]-1)
		density[(rand_particle + 1)] = (density[(rand_particle + 1)] + 1)
	
	return density

	

# comparison()
# Function that runs the comparisons
# Must compare the energies at both densities
# Must return a density as per the criteria in 4)


# monte_carlo()
# Function that repeats move_random and comparisons a given number of times
# Must also depend on the initial density and temperature