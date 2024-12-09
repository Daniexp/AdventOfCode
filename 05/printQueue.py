import argparse
import os
from collections import defaultdict

def fixPageOrder(order, pages):
	return pages

def correctOrder(rules, pages):
	pages.reverse()
	for i in range(len(pages)):
		postPages = pages[i + 1:]  # Más claro que filtrar con índices manualmente
		if any(page in postPages for page in rules.get(pages[i], [])):
		        return False
	return True

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
	pages = list()
	order = defaultdict(list)
	try:
		with open(args.file, "r") as f:
			data = f.read()
			data = data.split("\n\n")
			if len(data) != 2:
				raise ValueError("File doens't contain rules and updates to pages.")
			rules = data[0].split("\n")
			for rule in rules:
				nmbs = rule.split("|")
				order[int(nmbs[0])].append(int(nmbs[1]))
			updates = data[1].split("\n")
			updates.pop()
			for upd in updates:
				nmbs = upd.split(",")
				nmbs = [int(nmb) for nmb in nmbs]
				pages.append(list(nmbs))
	except Exception as e:
		print(f"Error: {e}")
		exit(1)
	total_middle = 0
	total_middle_incorrect = 0
	for update in pages:
		if correctOrder(order, update):
			total_middle += update[len(update) // 2]
		else:
			total_middle_incorrect += fixPageOrder(order, update)[len(update) // 2]
			
	print(f"Total middle pages is {total_middle}")
	print(f"Total middle incorrect pages is {total_middle_incorrect}")

if __name__ == "__main__":
	main()
