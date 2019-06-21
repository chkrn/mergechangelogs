#!/usr/bin/env python3

import difflib
import io
import unittest
from mergechangelogs import merge_changelogs

class TestMerge(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		with open('test/Changelog_expect.md') as file:
			cls.expectation = file.read().splitlines(True)

	@classmethod
	def run_with_files(cls, *input_files_paths):
		output = io.StringIO()
		merge_changelogs(output, input_files_paths)
		diff = difflib.unified_diff(output.getvalue().splitlines(True), cls.expectation)
		output.close()

		print('LLL', ''.join(diff), 'JJJ')

	def test_succesfully_merge(self):
		self.run_with_files('test/Changelog_1.md', 'test/Changelog_2.md', 'test/Changelog_3.md')

	def test_fail_merge(self):
		self.run_with_files('test/Changelog_1.md', 'test/Changelog_2.md')

if __name__ == '__main__':
	unittest.main()

