title: Adding, Committing, and Pushing
author: Jarrod Millman
date: 2014-02-14
slug: lab03

In this lab, you will:

1. Work on the cloud
2. Complete your assignment
3. Submit your assignment

**Note:**  There is a short review for using `git` and seeing your
grades at the bottom of the lab.  You may also want to review previous
labs if you are uncertain about using `git`.

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

You will need to start working on the cloud machine, since for your
midterm and final you will be required to work on the cloud.  If you don't
practice on it, you may find that you run into problems that could
negatively impact your grade.

First, open your Bash terminal and make sure you are in the top-level
directory of your lab repository.  Check where you are using the `pwd`
command. 

If you haven't been working on the cloud for the labs, you may first need
to create your "src" directory using `mkdir ~/src` .  Then configure
`git` using `git config` and clone your Github repo to your cloud account
using `git clone`.  You can refer to  [lab 1](lab01) for more details, but
you will basically need to run the following commands (where you've
replaced the details in `< >` with your own information):

```bash
mkdir ~/src
cd ~/src
git config --global user.name "<Jarrod Millman>"
git config --global user.email "<millman@berkeley.edu>"
git clone https://github.com/<jarrodmillman>/stat133.git 
``` 

If you have been working on the cloud, just `cd` to the correct directory
and then do a `git pull` to pull the changes in the remote Github repo
into your local repository.

## Complete your assignment

Now that you have pulled from your Github repo, you should see a
new file called `lab3.py`.  Open this with your text editor.  At
the top of the file you will see:

```python
dna = 'ATGATTTTTCCATCTTTAAGTGCGATACTGTTTTGT'
dna_bases = ['A', 'C', 'G', 'T']
rna_bases = ['A', 'C', 'G', 'U']
basecomplement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

def is_dna(dna):
    """
    Checks whether a string is a DNA string.

    Parameters
    ----------
    dna : string
        A string (i.e., you can assume you get a string)

    Returns
    -------
    out : bool
        Returns True, is dna is a valid DNA string (i.e,
        a string composed of the letters 'A', 'C', 'G', or
        'T' (and False otherwise).

    Hint
    ----
    You may want to iterate over the string checking each character.

    Examples
    --------
    >>> is_dna('ATGATT')
    True
    >>> is_dna('ATGATU')
    False
    >>> is_dna('atgatt')
    False
    >>> is_dna('My grandMa')
    False
    """
    return NotImplemented
```

This is followed by several additional function stubs.  Your assignment
is to replace the body of each function (i.e., `return NotImplemented`)
with valid Python code that behaves as specified by the docstring.

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

## Review:  `git`

Here are the `git` commands you will use in this class:

```bash
$ git
usage: git <command> [<args>]

The most commonly used git commands are:
   add        Add file contents to the index
   config     Get and set repository or global options
   clone      Clone a repository into a new directory   
   commit     Record changes to the repository
   log        Show commit logs
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects
   status     Show the working tree status

'git help -a' and 'git help -g' lists available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
```

When you try this on your computer, you will see much more information.

1. At the start of each lab, use `git pull` from inside your local repository
2. Use `git add` and `git commit` to add and commit new files or changes
   to existing files in your repository
3. Use `git push` to push your changes to Github so that I can see your
   work and assign grades
4. Repeat the following week

## Review:  How can I see my grade?

**Note:** I haven't submitted the grades for lab2 yet.

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

You can write a script based on the one you  wrote for [lab 2](lab02) to
process your `grades.json` file printing out this information in whatever
format you please, calculate and report statistics, or plot your scores.
