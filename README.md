# mergechangelogs.py
For example, we have Changelog files:
* ./test/1/CHANGELOG.MD:
```- One line without date

- Another line without date
## 1999-02-18
- Fix with header without spaces
## 2019-02-18
- Realized control of XX
- Fixed work with more than 80 YY
- Fixed work with ZZ > 1

## 2019-02-08
- Second project fix
- Second project second fix
- Second project new feature
## 2017-01-18


- Some old fix
- Very old fix


```

* ./test/2/CHANGELOG.md:
```- First line in second project
## 1999-02-18  
- Fix with header with spaces
## 2019-02-11
- Fixed some stuff
## 2019-02-08

- Some new stuff in first project:
    - One
        - one dot one
        - one dot two
        - one dot three
    - Two
        - two dot one
        - two dot two
        - two dot three
    
- Some fix in first project (string before contain only spaces)

## 2018-02-07

- Fixed something
- Something new
- Some more

```
Result will look like:
```- One line without date
- Another line without date
- First line in second project

## 2019-02-18

- Realized control of XX
- Fixed work with more than 80 YY
- Fixed work with ZZ > 1

## 2019-02-11

- Fixed some stuff

## 2019-02-08

- Second project fix
- Second project second fix
- Second project new feature
- Some new stuff in first project:
    - One
        - one dot one
        - one dot two
        - one dot three
    - Two
        - two dot one
        - two dot two
        - two dot three
- Some fix in first project (string before contain only spaces)

## 2018-02-07

- Fixed something
- Something new
- Some more

## 2017-01-18

- Some old fix
- Very old fix

## 1999-02-18

- Fix with header without spaces
- Fix with header with spaces
```
_File was generated with:
```./mergechangelogs.py --readme ./test/1/CHANGELOG.MD ./test/2/CHANGELOG.md```