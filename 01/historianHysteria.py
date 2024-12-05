import argparse
import os
from sortedcontainers import SortedList

def total_distance(cnt1, cnt2):
	res = 0
	for num1, num2 in zip(cnt1, cnt2):
		res += abs(num1 - num2)
	return res

def similarity_score(cnt1, cnt2):
	res = 0
	for num1 in cnt1:
		res += num1 * cnt2.count(num1)
	return res

def main():
	parser = argparse.ArgumentParser(
		description="Program that takes a file with two lines of positive integers and calculates the total distance between the pairs in order from smaller to the biggest one's between the number in the lines of the file."
	)
	parser.add_argument(
		"file",
		type=str,
		help="path to the file with positive integers"
	)
	args = parser.parse_args()
	if len(vars(args)) > 1 or not os.path.isfile(args.file):
		print("Error")
		exit(1)
	first = SortedList()
	second = SortedList()
	try:
		with open(args.file, "r") as f:
			for line in f:
				line = line.strip()
				parts = line.split()
				if len(parts) != 2:
					raise ValueError("Different than two numbers in the line");
				if not all(part.isdigit() and int(part) >= 0 for part in parts):
					raise ValueError("No valid number in the line");
				first.add(int(parts[0]))
				second.add(int(parts[1]))
	except Exception as e:
		print("Error: {e}")
		exit(1)
	print(f"Total distance is {total_distance(first, second)}")
	print(f"Similarity score is {similarity_score(first, second)}")

if __name__ == "__main__":
	main()
