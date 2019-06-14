#!/usr/bin/env python3

import sys

def merge_changelogs(output, input_files_paths):
	content_without_chapter = []
	chapters = {}

	for file_name in input_files_paths:
		chapter_content = content_without_chapter
		with open(file_name) as file:
			line = file.readline()
			while line:
				if line.startswith('##'):
					line = line.rstrip()
					chapter_content = chapters.get(line)
					if not chapter_content:
						chapters[line] = chapter_content = []
				elif not line.isspace():
					chapter_content.append(line)
					
				line = file.readline()

	for line in content_without_chapter:
		output.write(line)
	for chapter_content in reversed(sorted(chapters.keys())):
		output.write('\n{}\n\n'.format(chapter_content))
		for line in chapters[chapter_content]:
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
		for n, file_name in enumerate(input_files_paths):
			output.write('\n* File #{} ({}):\n```markdown\n'.format(n + 1, file_name))
			with open(file_name) as file:
				output.write(file.read())
			output.write('```')
		output.write('\nResult will look like:\n```markdown\n')

	merge_changelogs(output, input_files_paths)

	if readme_mode:
		output.write('```\n_File was generated with:_\n```{}```'.format(" ".join(sys.argv)))
