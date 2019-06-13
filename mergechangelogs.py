#!/usr/bin/env python3

import sys

def merge_changelogs(output, input_files_paths):
	lines_without_chapter = []
	chapters = {}

	for file_name in input_files_paths:
		chapter = lines_without_chapter
		with open(file_name) as file:
			line = file.readline()
			while line:
				if line.startswith('##'):
					line = line.rstrip()
					chapter = chapters.get(line)
					if not chapter:
						chapter = []
						chapters[line] = chapter
				elif not line.isspace():
					chapter.append(line)
					
				line = file.readline()

	for line in lines_without_chapter:
		output.write(line)
	for chapter in reversed(sorted(chapters.keys())):
		output.write('\n')
		output.write(chapter)
		output.write('\n\n')
		for line in chapters[chapter]:
			output.write(line)

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print('Usage:\n', sys.argv[0], 'input_files_paths', file=sys.stderr)
		sys.exit(2)

	merge_changelogs(sys.stdout, sys.argv[1:])

