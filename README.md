# mergechangelogs.py
For example, we have Changelog files:
* examples/Changelog_1.md:
```markdown
- File 1, item 3
## 2019-01-02
- File 1, item 2
## 2019-01-01
- File 1, item 1
```
* examples/Changelog_2.md:
```markdown
- File 2, item 3
## 2019-01-03
- File 2, item 2
## 2019-01-02
- File 2, item 1
```Result will look like:
```markdown
- File 1, item 3
- File 2, item 3

## 2019-01-03

- File 2, item 2

## 2019-01-02

- File 1, item 2
- File 2, item 1

## 2019-01-01

- File 1, item 1
```
_File was generated with:_
```./mergechangelogs.py --readme examples/Changelog_1.md examples/Changelog_2.md```