#!/usr/bin/env python3
""" See README.md """

import argparse
import sys

def merge_changelogs(output, input_files_paths):
	""" Merges input_files_paths to output object (object must have write() method)"""

	content_without_chapter = []
	chapters = {}

	for file_name in input_files_paths:
		chapter_content = content_without_chapter
		with open(file_name) as file:
			for line in file:
				if line.startswith('##'):
					line = line.rstrip()
					chapter_content = chapters.get(line)
					if not chapter_content:
						chapters[line] = chapter_content = []
				elif not line.isspace():
					chapter_content.append(line)

	for line in content_without_chapter:
		output.write(line)
	for chapter_content in reversed(sorted(chapters.keys())):
		output.write('\n{}\n\n'.format(chapter_content))
		for line in chapters[chapter_content]:
			output.write(line)

def __main():
	output = sys.stdout

	parser = argparse.ArgumentParser()
	parser.add_argument('-r', '--readme', action='store_true', help='generate readme file')
	parser.add_argument('input_files_paths', nargs='+')
	args = parser.parse_args()

	if args.readme:
		output.write('# mergechangelogs.py\nFor example, we have Changelog files:')
		for i, file_name in enumerate(args.input_files_paths):
			output.write('\n* File #{} ({}):\n```markdown\n'.format(i + 1, file_name))
			with open(file_name) as file:
				output.write(file.read())
			output.write('```')
		output.write('\nResult will look like:\n```markdown\n')

	merge_changelogs(output, args.input_files_paths)

	if args.readme:
		output.write('```\n_File was generated with:_\n```{}```'.format(" ".join(sys.argv)))

if __name__ == '__main__':
	__main()

