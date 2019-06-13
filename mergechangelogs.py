#!/usr/bin/env python3

def test():
	chapters = {}
	files = ("test/1/CHANGELOG.MD", "test/2/CHANGELOG.md")
	for i in files:
		with open(i) as file:
			line = file.readline()
			while line:
				if line.startswith("##"):
					line = line.rstrip()
					chapter = chapters.get(line)
					if not chapter:
						chapter = []
						chapters[line] = chapter
				else:
					chapter.append(line)
					
				line = file.readline()

	for chapter in sorted(chapters.keys()):
		print(">> " + chapter)
		for line in chapters[chapter]:
			print("> " + line, end = "")

if __name__ == "__main__":
	test()

