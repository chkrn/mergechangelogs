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
	def run_with_files(cls, input_files_paths):
		"""
		Returns:
			str: Diff between merge (of files in input_files_paths) result and expectation;
				or empty string, if diff is empty.
		"""
		print('\nRunning test with files', input_files_paths)
		output = io.StringIO()
		merge_changelogs(output, input_files_paths)
		return ''.join(difflib.unified_diff(output.getvalue().splitlines(True), cls.expectation))


	def test_fail_merge(self):
		diff = self.run_with_files(['test/Changelog_{}.md'.format(n + 1) for n in range(2)])
		self.assertTrue(diff)

	def test_succesfully_merge(self):
		diff = self.run_with_files(['test/Changelog_{}.md'.format(n + 1) for n in range(3)])
		print('Expected empty diff:<diff>{}</diff>'.format(diff))
		self.assertFalse(diff)

	def test_non_existent_file(self):
		with self.assertRaises(FileNotFoundError):
			self.run_with_files(['test/Changelog_{}.md'.format(n + 1) for n in range(4)])

if __name__ == '__main__':
	unittest.main()

