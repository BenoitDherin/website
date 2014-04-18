title: Working with docstrings and tests 
author: Jarrod Millman
date: 2014-02-21
slug: lab04

In this lab, you will:

1. Work on the cloud
2. Complete your assignment
3. Submit your assignment

**Note:**  Several people had issues with indentation last week.
This was due to using tabs.  You should always use space when
indenting Python code.  The recommended standard is to use 4 spaces
for each code level.
See [this](http://legacy.python.org/dev/peps/pep-0008/#tabs-or-spaces)
for more details.

**Workflow recap:** This workflow may take some time to become accustomed
to, but this is the basic process you will use for the rest of the
semester:

1. At the start of each lab, use `git pull` from inside your local
   repository (or `git clone` if you don't have a local repository)
2. Use `git add` and `git commit` to add and commit new files or changes
   to existing files in your repository (you can use `git status`
   and `git log` to make sure you know what is going on with your
   repo)
3. Use `git push` to push your changes to Github so that I can see your
   work and assign grades
4. Repeat the following week

## Work on the cloud

I will assume you are working on the cloud.  So all the commands assume
you are on the cloud.

First, open your Bash terminal and make sure you are in the top-level
directory of your lab repository.  Check where you are using the `pwd`
command.  If you aren't in the correct directory, just `cd` to the
correct directory. Once you are in the correct directory, you should
use `git pull` to pull the changes on the remote Github repo
into your local repository.

## Complete your assignment

Now that you have pulled from your Github repo, you should see a
new file called `lab4.py`.  Open this with `gedit`.  At
the top of the file you will see:

```python
"""
This is lab 4.  Please do *not* remove any of the docstrings
from this document.  Docstrings are an important part of a
Python program:

    A docstring is a string literal that occurs as the first
    statement in a module, function, class, or method definition.
    Such a docstring becomes the __doc__ special attribute of
    that object.

```

This is followed by a class stub.  Your assignment
is to replace the body of the function (i.e., find all
instances of `return NotImplemented` and replace with working
code) with valid Python code that behaves as specified by
the docstring.

Please don't remove the docstrings.  You can read more about
them at the top of `lab4.py`.  The docstrings include tests,
which you can use to test your implementation as you go.

To run all the doctests, you can type the following:

```bash
$ python lab4.py -v
Trying:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
Expecting nothing
ok
Trying:
    alphabet[::-1]
Expecting:
    'zyxwvutsrqponmlkjihgfedcba'
ok

```

You will see much more than this on your computer.  The `-v`
option runs the tests in verbose mode.  This means that it will
print out information even when the tests pass.  By default,
it will only print out information when there are errors:

```bash
$ python lab4.py 
**********************************************************************
File "lab4.py", line 76, in __main__.Cipher
Failed example:
    reverse = Cipher("reverse")
Exception raised:
    Traceback (most recent call last):
      File "/usr/lib64/python2.7/doctest.py", line 1289, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.Cipher[0]>", line 1, in <module>
        reverse = Cipher("reverse")
    TypeError: __init__() should return None, not 'NotImplementedType'
**********************************************************************
```

You should run `python lab4.py`, find an error, try to fix it,
and rerun `python lab4.py`.  Once you have no errors, you will
see this:

```bash
$ python lab4.py
$
```

This is because everything passed.  To double-check that everything
passed, use the `-v` option:

```bash
$ python lab4.py -v
Trying:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
Expecting nothing
ok
Trying:
    alphabet[::-1]
Expecting:
    'zyxwvutsrqponmlkjihgfedcba'
ok
  ....  <snip>  ....

Trying:
    hybrid.encrypt("abcdefghijklmnopqrstuvwxyz")
Expecting:
    'nmlkjihgfedcbazyxwvutsrqpo'
ok
4 items had no tests:
    __main__.Cipher.__init__
    __main__.Cipher.decrypt
    __main__.Cipher.encrypt
    __main__.Cipher.isvalid
2 items passed all tests:
  10 tests in __main__
  10 tests in __main__.Cipher
20 tests in 6 items.
20 passed and 0 failed.
Test passed.
```

## Submit your work

You will submit your work using `git push` to put a complete
copy of your local repo on Gitub, so that I can see it.

First you will need to `add` and `commit` all the work you
wish to submit to your local repository.  You should use
`git status` and `git log` to make sure your repository is in
the state you expect.

Once your local repository is in whatever state you wish,
you just need to push your local repository up to your remote
Github repo using `git push`.

