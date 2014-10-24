"""Test file for Monte-Carlo"""

# contains the tests for the Monte-Carlo functions
from nose.tools import assert_equal, assert_almost_equal, assert_true, assert_raises


"""Tests for move_random"""
# move_random should pass the following tests

from monte_carlo_functions import move_random


def test_no_particles():
	# move_random on a empty density should return a empty density
	densities = [ [0], [0, 0, 0, 0] ]
	for density in densities: assert_equal(move_random(density), density)
  
   
def test_move_random():
	from numpy.random import randint

	# create a random density of length between 2 and 10
	density_length = randint(2, 10)
	density = randint(0, 50, size = density_length)
	
	# move_random should not change the total number of particles 
	assert_equal(sum(density), sum(move_random(density)))
	

def test_compare_energies():
	from monte_carlo_functions import compare_energies
	from numpy.random import randint
	from numpy import absolute
	
	density_length = randint(2, 10)
	density = randint(0, 50, size = density_length)
	
	T = randint (1, 100)
	
	# compare_energies moves at most 1 particle 
	for index in (0, density_length - 1):
		assert absolute((compare_energies(density, T))[index] - (compare_energies(move_random(density), T))[index]) <= 1