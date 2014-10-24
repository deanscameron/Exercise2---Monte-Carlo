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
	from numpy import sum, nonzero, absolute, array
	import operator
  
	# create a random density of length between 2 and 10
	density = randint(0, 50, size = randint(2, 10))
	
	# move_random should not change the total number of particles 
	assert_equal(sum(density), sum(move_random(density)))
	
	# move_random should only effect 2 indices
	difference = move_random(density) - density
	assert_equal(len(nonzero((difference)[0]), 2)
	
	# the two indices should change by +1 and -1
	assert_equal(reduce(operator.mul, difference, 1), -1)