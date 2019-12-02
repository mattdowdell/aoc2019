#! /usr/bin/env python3

"""
"""

import sys


def main():
	"""Program entry point."""
	data = [int(x.strip()) for x in sys.stdin.read().strip().split(",")]
	found = False
	target = 19690720

	for noun in range(100):
		for verb in range(100):
			output = search(data[:], noun, verb)

			if output == target:
				answer = 100 * noun + verb
				print(f"noun: {noun}, verb: {verb}")
				print(f"answer: {answer}")
				return


def search(data: list, noun: int, verb: int) -> int:
	"""
	"""
	index = 0

	# initial setup
	data[1] = noun
	data[2] = verb

	while index < len(data):
		opcode = data[index]
		left_pos = data[index + 1]
		right_pos = data[index + 2]
		ret_pos = data[index + 3]

		left = data[left_pos]
		right = data[right_pos]

		if opcode == 1:
			val = left + right
			data[ret_pos] = val

		elif opcode == 2:
			val = left * right
			data[ret_pos] = val

		elif opcode == 99:
			break

		else:
			raise RuntimeError(f"Unknown opcode: {opcode}")

		index += 4

	return data[0]


if __name__ == "__main__":
	main()
