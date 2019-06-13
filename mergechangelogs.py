#!/usr/bin/env python3

def merge_changelogs(output_file_path, *input_files_paths):
	lines_without_chapter = []
	chapters = {}

	for file_name in input_files_paths:
		chapter = lines_without_chapter
		with open(file_name) as file:
			line = file.readline()
			while line:
				if line.startswith("##"):
					line = line.rstrip()
					chapter = chapters.get(line)
					if not chapter:
						chapter = []
						chapters[line] = chapter
				elif not line.isspace():
					chapter.append(line)
					
				line = file.readline()

	with open(output_file_path, 'w') as file:
		for line in lines_without_chapter:
			file.write(line)
		for chapter in reversed(sorted(chapters.keys())):
			file.write('\n')
			file.write(chapter)
			file.write('\n\n')
			for line in chapters[chapter]:
				file.write(line)

if __name__ == "__main__":
	merge_changelogs("CHANGELOG.md", "test/1/CHANGELOG.MD", "test/2/CHANGELOG.md")

