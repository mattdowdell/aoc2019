#! /usr/bin/env python3

"""Calculate the fuel required to launch a given module.

For a module of weight ``x``, the mass of the fuel required is ``floor(x / 3) - 2``. However, as
this fuel has mass as well, then the solution must also account for the fuel required to launch the
additional fuel.

Usage:

  $ ./day1.py < input.txt
"""

import math
import sys


def main():
	"""Program entry point."""
	values = [int(line.strip()) for line in sys.stdin.readlines()]
	output = sum([calc_mass(val) for val in values])

	print("Fuel mass:", output)


def calc_mass(mass: int) -> int:
	"""Recursively calculate the fuel required to launch the given mass.

	:param int mass: The mass to launch.

	:return: The fuel required to launch the ``mass``.
	:rtype: int
	"""
	fuel = int(math.floor(mass / 3.0)) - 2

	if fuel <= 0:
		return 0

	return fuel + calc_mass(fuel)


if __name__ == "__main__":
	main()
