#!/usr/bin/env python3

def test():
	files = ("test/1/CHANGELOG.MD", "test/2/CHANGELOG.md")
	for i in files:
		with open(i) as file:
			line = file.readline()
			while line:
				if line.startswith("##"):
					print(">> " + line, end="")
				else:
					print("> " + line, end="")
				line = file.readline()

if __name__ == "__main__":
	test()

