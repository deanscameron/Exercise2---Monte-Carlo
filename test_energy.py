"""Test file for the energy function"""

# Contains tests for the energy function
# Use tests from the Classroon Exercise

from nose.tools import assert_raises, assert_almost_equal
from monte_carlo_functions import energy


def test_zero_energy_no_particles():
  # Zero energy for no particles
  densities = [ [], [0], [0, 0, 0, 0] ]
  for density in densities: assert_almost_equal(energy(density), 0)

  # Zero energy for zero coefficient
  assert_almost_equal(energy([1, 1, 1], coefficient=0), 0)

def test_derivative():
  from numpy.random import randint

  # Loop over vectors of different sizes
  for vector_size in randint(1, 1000, size=30): 

    # Create random density of size N
    density = randint(50, size=vector_size)

    # will do derivative at this index
    element_index = randint(vector_size)

    # modified densities
    density_plus_one = density.copy()
    density_plus_one[element_index] += 1

    # Compute and check result
    expected = density[element_index] if density[element_index] > 0 else 0
    actual = energy(density_plus_one) - energy(density) 
    assert_almost_equal(expected, actual)

def test_derivative_no_self_energy():
  # If particle is alone, then its participation to energy is zero
  from numpy import array

  density = array([1, 0, 1, 10, 15, 0])
  density_plus_one = density.copy()
  density[1] += 1 

  expected = 0
  actual = energy(density_plus_one) - energy(density) 
  assert_almost_equal(expected, actual)