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
	output = sys.stdout

	if len(sys.argv) > 1 and sys.argv[1] == '--readme':
		input_files_paths = sys.argv[2:]
		readme_mode = True
	else:
		input_files_paths = sys.argv[1:]
		readme_mode = False

	if len(input_files_paths) == 0:
		print('Usage:\n', sys.argv[0], '[--readme] input_files_paths', file=sys.stderr)
		sys.exit(2)

	if readme_mode:
		output.write('# mergechangelogs.py\nFor example, we have Changelog files:')
		for file_name in input_files_paths:
			output.write('\n* ' + file_name + ':\n```')
			with open(file_name) as file:
				output.write(file.read())
			output.write('```\n')
		output.write('Result will look like:\n```')

	merge_changelogs(output, input_files_paths)

	if readme_mode:
		output.write('```\n_File was generated with:\n```' + " ".join(sys.argv) + '```')
