#!/usr/bin/env python3

def test():
	with open('test/1/CHANGELOG.MD') as file:
		line = file.readline()
		while line:
			if line.startswith("##"):
				print(">> " + line, end="")
			else:
				print("> " + line, end="")
			line = file.readline()

if __name__ == "__main__":
	test()

