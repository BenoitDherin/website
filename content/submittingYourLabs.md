title: Submitting your labs 
author: Jarrod Millman
date: 2014-02-07
slug: lab02

In this lab, you will:

1. Take your next steps with `git`
2. Get your grade for lab 1
3. Learn about Python dictionaries
4. Write a little grade reporting program
5. Submit your work for lab 2

You will need:

1. A Github educational account
2. If you are using your own laptop, please install relevant [software](pages/software)
3. To have completed [lab 1](lab01)

## First things first

**NOTE: Pay close attention to this section and ask for clarification if you
don't understand any of the steps.  Each lab will begin the same way each week.
But in future weeks, I won't provide these details and will expect you to be
able to get to your repository with out additional instructions.**

First, open your Bash terminal and make sure you are in the top-level directory
of your lab repository.  Check where you are using the ```pwd``` command.  This
is a command that you will use all the time as you become more proficient at
working on the commandline to make sure you are where you are supposed to be
in the filesystem hierarchy.

If you aren't in the correct directory, you need to change your working directory
using the ```cd``` command.  This is another very important command that you will
use regularly.  If you put your repository in the directory I suggested last week,
you should type the following (if not, you will need to change the command below
accordingly):

```bash
cd ~/src/stat133
```

As a further check, take a look at your ```git log```:

```bash
$ git log 
commit bbc329fe5f0672582a3ad3c70f5b86f4acc15f63
Author: Jarrod Millman <jarrod.millman@gmail.com>
Date:   Wed Jan 29 14:19:38 2014 -0800

    Add personal info

commit dead6f41c65e50f444760653205e21083caabfcc
Author: Jarrod Millman <jarrod.millman@gmail.com>
Date:   Tue Jan 28 22:29:33 2014 -0800

    Initial commit
```

If you haven't done any additional ```git commit```s since last week, this log
should be identical to the results you saw at the end of the previous lab.

## Next steps with ``git``

Last week, you used the following ``git`` commands:

```bash
$ git
usage: git <command> [<args>]

The most commonly used git commands are:
   add        Add file contents to the index
   config     Get and set repository or global options
   clone      Clone a repository into a new directory   
   commit     Record changes to the repository
   log        Show commit logs
   push       Update remote refs along with associated objects
   status     Show the working tree status

'git help -a' and 'git help -g' lists available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
```

When you try this on your computer, you will see much more information.  As you
will recall, I reduced the output so that it only contains commands that you used
last week.  Please read the above output carefully and try to remember how you used
these commands last week and what they did.  You've already used ```git log```
again and you will use all the above commands again today (as well as in every
other lab) with the exception of ```git config``` and ```git clone```.  Since
you have already configured ```git``` and ```cloned``` your repository from
Github, you won't need to do that again unless you are working on a different
computer.

Today you will learn one more command:  ```git pull```.  Type ```git pull --help```
at your Bash prompt and you will see something similar to this (to exit this
you will need to type `q` for quit):

```bash
$ git pull --help

NAME
       git-pull - Fetch from and integrate with another repository or a
       local branch

SYNOPSIS
       git pull [options] [<repository> [<refspec>...]]

DESCRIPTION
       Incorporates changes from a remote repository into the current
       branch. In its default mode, git pull is shorthand for git fetch
       followed by git merge FETCH_HEAD.
```

As you can see, `git pull` will incorporate changes from a remote
repository (in your case, your Github repository).  Since last week,
I've **cloned** everyone's repositories onto my laptop where I used a script
to test whether everyone correctly completed the first lab.  I assigned
grades to everyone and **committed** a file named `grades.json` to
my copy of your repository that is on my computer.  Then, so you can
see the changes I made, I **pushed** my changes back to Github.

In order for you to see your grade, you will need to **pull** my changes
to your local repository from Github:

```bash
$ git pull
```

If everything goes successfully, you will now have an updated copy
of the repository.  Use `git log` to see a more detailed log
of the changes.  For some of you, there may be a conflict with
what you have on your computer and what is on Github.  If you have
any problems, please ask me for help before continuing.

This workflow may take some time to become accustomed to, but this is
the basic process you will use for the rest of the semester:

1. At the start of each lab, use `git pull` from inside your local repository
2. Use `git add` and `git commit` to add and commit new files of changes
   to existing files in your repository
3. Use `git push` to push your changes to Github so that I can see your
   work and assign grades
4. Repeat the following week

## How can I see my grade?

List the contents of your repository:

```bash
$ ls
grades.json  info.py  info.pyc  README.md
```

You should have a file named `grades.json`.  To see the content of
this file, use the `cat` command:

```bash
$ cat grades.json 
{
    "email": "me@school.edu", 
    "grades": {
        "lab1": {
            "earned": 12, 
            "possible": 12
        }
    }, 
    "id": "0123456789", 
    "login": "me", 
    "name": "Full Name", 
    "url": "git@github.com:me/stat133.git"
}
```

This should be fairly (human-)readable, but you will notice that there are
a lot of additional characters that you would probably not use if you were
just writing this information yourself.  The extra characters are there
because this is specific data format called [JSON](http://www.json.org/).
If you are interested, you can follow the above link and read more about
this format.  But it isn't necessary for you to know anything more at this
point other than this is a format that will allow you to load this data
into Python as a dictionary.

In this lab, you are going to learn more about Python dictionaries and
write a little Python program that will read this file and print out
a little summary of your grades to the terminal.

## Python dictionaries

Python [dictionaries](http://docs.python.org/2/tutorial/datastructures.html#dictionaries)
provide a very useful data structure.  Let's look at a simple example.

Imagine that you want to use Python to store phone numbers.  You might
create a data structure like this:

```python
tel = {'name': "Jarrod Millman",
       'number': '555-1234'}
```

Let's see how this works at the IPython terminal (as opposed to
notebook) command prompt"

```python
$ ipython 
Python 2.7.5 (default, Nov 12 2013, 16:45:54) 
Type "copyright", "credits" or "license" for more information.

IPython 0.13.2 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: tel = {'name': "Jarrod Millman",
   ...:        'number': '555-1234'}

In [2]: tel['name']
Out[2]: 'Jarrod Millman'

In [3]: tel['number']
Out[3]: '555-1234'
```

What if you want to store multiple phone numbers per person?  You
could do something like this:

```python
tel = {'name': "Jarrod Millman",
       'numbers': {
          'home': '555-1234',
          'cell': '555-1235'
       }
      }
```

Let's try this at the IPython prompt:

```python
In [4]: tel = {'name': "Jarrod Millman",
   ...:        'numbers': {
   ...:           'home': '555-1234',
   ...:           'cell': '555-1235'
   ...:        }
   ...:       }

In [5]: tel['name']
Out[5]: 'Jarrod Millman'

In [6]: tel['numbers']
Out[6]: {'cell': '555-1235', 'home': '555-1234'}

In [7]: tel['numbers']['cell']
Out[7]: '555-1235'

In [8]: tel['numbers']['home']
Out[8]: '555-1234'
```

## Lab 2 program

Now that you have a local copy of your repo, you will need to add
some new content before submitting your new lab assignment.

Before adding anything, use the `tree` command to see how your
repository directory structure looks.

```bash
$ tree
.
├── grades.json
├── info.py
└── README.md

0 directories, 3 files
```

**Note: You may not have `tree` installed.  If not, you
can use `ls` to list the content of your directory.**

Next, you will need to create some subdirectories.

```bash
$ mkdir -p lab2/data
```

Note that you need to use the `-p` option to create `lab2` and
a subdirectory of `lab2` named `data` in one command.  Without
the `-p` option `mkdir` will complain:

```bash
$ mkdir  lab2/data
mkdir: cannot create directory ‘lab2/data’: No such file or directory
```

This error message occurs because the `mkdir` command without the `-p`
option will try to create the subdirectory `data` inside the directory
`lab2`, which doesn't exist yet.  The `-p` options tells `mkdir `

```bash
$ tree
.
├── grades.json
├── info.py
├── lab2
│   └── data
└── README.md

2 directories, 3 files
```

Next you need to write a Python script that creates a Python
dictionary of grades and saves that information to `data/test.json`.

Make sure you are in the lab2 directory (reminder: use `pwd` to find
out where you are and `cd` to change your working directory).  Next,
open your text editor and create a new file, called `mkgrade.py`.

---

**Note:** If you are on MacOS, you should be able to type:
`edit mkgrade.py`.  If you are on Windows, you will first need to
add the following lines to your `~/.bashrc` file:

```bash
export PATH=/c/Program\ Files/Notepad++:$PATH
alias edit='notepad++'
```

On some computers you will need to add this instead:

```bash
export PATH=/c/Program\ Files\ \(x86\)/Notepad++:$PATH
alias edit='notepad++'
```

If you have any problems with this step, please ask for assistance.
I will expect everyone to be able to open their text editor
from the Bash prompt using the command `edit`.  So please
don't skip this step.

In order for Bash to execute this code, type:

```bash
$ . ~/.bashrc
```

Now Windows users should be able to type: `edit mkgrade.py` as well.
If you have any troubles with this step, please ask for help.

---

Now add the following content to `mkgrade.py`:

```python
# First import the Python JSON package
import json

student = {"name": "Student A",
          "grades": {
            "lab1": {
                "earned": 9,
                "possible": 12},
            "lab2": {
                "earned": 12,
                "possible": 15},
            "lab3": {
                "earned": 20,
                "possible": 22},
        },
}

#### begin CORRECTION NEEDED
outfile = # open the file 'data/test.json' for writing
json.dump(student, outfile, sort_keys = True, indent = 4)
# close the file
#### end CORRECTION NEEDED
```

Save this file and trying running it from the commandline:

```bash
$ python mkgrade.py 
  File "mkgrade.py", line 19
    outfile = # open the file 'data/test.json' for writing
                                                         ^
SyntaxError: invalid syntax
```

You should get the error message displayed above.  Before
continuing you need to correct the script.

At the bottom of the file, you need to add some code to
open and close the file.  I've already added the line
needed to write the `grades` dictionary to the file:
(i.e., `json.dump(student, outfile, sort_keys = True, indent = 4)`).

Open the script back up with your text editor and correct
the errors so that the script correctly creates the
necessary file.

Once you've corrected the script, you will need to close
your editor and run the script from the commandline:

```bash
python mkgrade.py
```

This time you shouldn't get any message from Bash.  It
should just run the script as you asked it to and when
it finishes provide you with a new prompt.

To make sure you've done everything correctly, you
should verify that you've created the necessary file
and that it has the correct content using the `cat`
command:

```bash
$ cat data/test.json 
{
    "grades": {
        "lab1": {
            "earned": 9, 
            "possible": 12
        }, 
        "lab2": {
            "earned": 12, 
            "possible": 15
        }, 
        "lab3": {
            "earned": 20, 
            "possible": 22
        }
    }, 
    "name": "Student A"
}
```

Now that you've created a test grade file with multiple
grades, you will create another script `report.py` to read this file
and print a human readable message to the screen.

```python
import json

infile = # open the file 'data/test.json'
student = json.load(infile)
# close infile

name = student['name']
grades = student['grades']

print "." * 70
print name, grades['lab1']['earned'], grades['lab1']['possible']
```

Save your file and run it from the Bash prompt:

```bash
$ python report.py 
  File "report.py", line 3
    infile = # open the file 'data/test.json'
                                            ^
SyntaxError: invalid syntax
```

Now fix the top of the script so that it properly opens
`data/test.json` and closes it.  Once you've fixed the
script, save it and test it from the Bash prompt:

```bash
$ python report.py 
......................................................................
Student A 9 15
```

Finally, you need to edit your script so that it prints out the
information a little more useful manner and do it for all three
lab assignments.  Once you are done, run your script again.  Exactly
how you do this is up to you (except that you need to use the variables
rather than just cutting and pasting the text from below.  You are
done when your output looks like this:

```bash
$ python report.py 
......................................................................
Student A got a 9 out of 12 on lab1
Student A got a 12 out of 15 on lab2
Student A got a 20 out of 22 on lab3
......................................................................
``` 

You may want to review [Exercise 5: More Variables and Printing](http://learnpythonthehardway.org/book/ex5.html)
from *Learn Python the Hard Way*.

## Submit your work

Next you will query the status of your ``git`` repo:

```bash
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        lab2/

nothing added to commit but untracked files present (use "git add" to track)
```

You can also use the `tree` command again to make sure you have all
the necessary files (this is what it should look like if you run it
from the top-level directory of your repository:

```bash
$ tree
.
├── grades.json
├── info.py
├── lab2
│   ├── data
│   │   └── test.json
│   ├── mkgrade.py
│   └── report.py
└── README.md
```

In particular, you need to make sure that in your `lab2` directory
you have the following layout:

```bash
]$ tree
.
├── data
│   └── test.json
├── mkgrade.py
└── report.py

1 directory, 3 files
```

Next, you will need to add your new work:

```bash
git add lab2
```

Notice that you only need to add the top directory and
`git` automatically adds all the content of that directory.

You can check this by examining the status of your repo:

```bash
$ git status 
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   lab2/data/test.json
        new file:   lab2/mkgrade.py
        new file:   lab2/report.py
```

Everything looks good, so go ahead and commit your change:

```bash
$ git commit -m "Lab 2"
[master 129a55c] Lab 2
 3 files changed, 51 insertions(+)
 create mode 100644 lab2/data/test.json
 create mode 100644 lab2/mkgrade.py
 create mode 100644 lab2/report.py
```

Next take a look at a log of what's been done using
`git log`.

At this point all your work was done locally, so the last thing
you need to do is push these changes up to your remote Github
repo using `git push`.
