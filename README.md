# chengdu

This [git repo] contains examples for class.

The *builtin* folder contains Python scripts which can be run with Python's [builtin] functions and libraries.

The *science* folder contains [Jupyter notebooks]. These require extra Python [packages] listed in `requirements.txt`.

[git repo]: https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#ch02-git-basics-chapter
[builtin]: https://docs.python.org/
[Jupyter notebooks]: https://jupyter-notebook.readthedocs.io/
[packages]: https://packaging.python.org/


## links

For detailed information, see these links:

class textbook
https://automatetheboringstuff.com/

python functions
https://docs.python.org/3/library/functions.html

numpy basics
https://numpy.org/doc/stable/user/absolute_beginners.html

scipy tutorial
https://docs.scipy.org/doc/scipy/tutorial

pandas user guide
https://pandas.pydata.org/docs/user_guide

seaborn examples
https://seaborn.pydata.org/examples/

scikit-learn user guide
https://scikit-learn.org/stable/user_guide.htm



## choose a project folder

First, decide where you want to save this project.
Create a folder (also known as a _directory_) on your computer.
Name it whatever you want. Mine is:
```
~/code/chengdu/
```
On Windows, the `/` slashes will be `\` backslashes.
The path will start with `C:` or `D:` or something similar.
For example, it might look like this:
```
C:\Users\lenovo\code\chengdu
```
If you have `git` installed, then you can [clone] this repo.
You'll have your own personal copy of all the files,
all of my edits, and all of my mistakes.

[clone]: https://git-scm.com/docs/git-clone


## install dependencies

To install everything


[shell script]:



## VSCode (Visual Studio Code) notes

The official VSCode docs are here:
```
https://code.visualstudio.com/docs/python/run
```

### start a blank project

- Launch VSCode.
- In the File menu, click `Open folder`.
- Find and select your project folder.
- In the `EXPLORER` sidebar, right-click and choose `New file`.
- Create a file called `hello.py`. Add these lines to the file:
```
# First program
print("Hello, World!")
```
- Click CTRL-S (Mac: command-s on Mac) to save `hello.py`.
- Click CTRL-SHIFT-P (Mac: command-shift-p) to open the Command Palette.
- Search for `Python: Select Interpreter` and select it.
- Choose a Python interpreter or press ESC to close the popup.
- Click the ▶ button to run `hello.py`.

### run the Python REPL in VSCode

- Click CTRL-SHIFT-P (Mac: command-shift-p) to open the Command Palette.
- Search for `Python: Start Native Python REPL` and select it. This should open a new tab called `Python REPL`.
- Enter `2 + 2` and press Enter. It should return 4.
