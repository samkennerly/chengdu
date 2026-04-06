# chengdu

This [git repo] contains examples for class.

The **builtin** folder contains Python scripts which can be run with Python's [builtin] functions and libraries.

The **science** folder contains [Jupyter notebooks]. These require extra Python [packages] listed in `requirements.txt`.

[git repo]: https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#ch02-git-basics-chapter
[builtin]: https://docs.python.org/
[Jupyter notebooks]: https://jupyter-notebook.readthedocs.io/
[packages]: https://packaging.python.org/


## links

For detailed information, see these links:

- class textbook
https://automatetheboringstuff.com/
- python functions
https://docs.python.org/3/library/functions.html
- numpy basics
https://numpy.org/doc/stable/user/absolute_beginners.html
- scipy tutorial
https://docs.scipy.org/doc/scipy/tutorial
- pandas user guide
https://pandas.pydata.org/docs/user_guide
- seaborn examples
https://seaborn.pydata.org/examples/
- scikit-learn user guide
https://scikit-learn.org/stable/user_guide.htm


## choose a project folder

First, decide where you want to save this project.
Create a folder (also known as a _directory_) on your computer.
Name it whatever you want. Mine is:
```
~/code/chengdu/
```
On Windows, the `/` slashes will be `\` backslashes, and
the path will start with `C:` or `D:` or something similar.
For example, it might look like this:
```
C:\Users\lenovo\code\chengdu
```
If you have `git` installed, then you can [clone] this repo.
You'll have a copy of all the files, my edits, and my mistakes.

[clone]: https://git-scm.com/docs/git-clone


## install dependencies

The `mkvenv` file explains how to create a [virtual environment]
and install all required packages.

On my computer, the command to run Python 3 is `python3`.
On some computers, it's `python` without the `3`.

`mkvenv` is a [shell script].
On any [POSIX] operating system (Linux, BSD, macOS, 麒麟, etc.),
you can run it by entering this command in a terminal:
```
./mkvenv
```

[virtual environment]: https://docs.python.org/3/library/venv.html
[shell script]: https://www.dotlinux.net/linux-shell-scripting-tutorial/
[POSIX]: https://www.baeldung.com/linux/posix


## extra steps for VSCode users

_VSCode_ is a short name for an [IDE] called
_Microsoft Visual Studio Code_. The docs are here:
```
https://code.visualstudio.com/docs/python/run
```
**Caution:** The official docs are often wrong.

[IDE]: https://github.com/resources/articles/what-is-an-ide


### start a blank project

- Launch VSCode.
- In the File menu, click `Open folder`.
- Select your project folder. (Mine is `~/code/chengdu`.)
- In the `EXPLORER` sidebar, right-click and choose `New file`.
- Create a file called `hello.py`. Add these lines to the file:
```
# First program
print("Hello, World!")
```
- Click CTRL-S to save `hello.py`.
- Click CTRL-SHIFT-P to open the Command Palette.
- Search for `Python: Select Interpreter` and select it.
- Choose a Python interpreter or press ESC to close the popup.
- Click the ▶ button to run `hello.py`.

### run the Python REPL

**REPL** is Python's _Read-Evaluate-Print-Loop_.
It's what you see when you run `python` or `python3`.
Here's how to run the REPL in VSCode:

- Click CTRL-SHIFT-P (Mac: command-shift-p) to open the Command Palette.
- Search for `Python: Start Native Python REPL` and select it. This should open a new tab called `Python REPL`.
- Enter `2 + 2` and press Enter. It should return 4.













