# chengdu

This [git repo] contains examples for class.

The **builtin** folder contains Python scripts which can be run with Python's [builtin] functions and libraries.

The **science** folder contains [Jupyter notebooks]. These require extra Python [packages] listed in `requirements.txt`.

[git repo]: https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#ch02-git-basics-chapter
[builtin]: https://docs.python.org/
[Jupyter notebooks]: https://jupyter-notebook.readthedocs.io/
[packages]: https://packaging.python.org/


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
and install all required packages. `mkvenv` is a [shell script].
On any [POSIX] operating system (Linux, BSD, macOS, 麒麟, etc.),
you can run it by entering this command in a terminal:
```
./mkvenv
```

**Caution:** On my computer, the command to run Python 3 is `python3`. On some computers, it's `python` without the `3`.

[virtual environment]: https://docs.python.org/3/library/venv.html
[shell script]: https://www.dotlinux.net/linux-shell-scripting-tutorial/
[POSIX]: https://www.baeldung.com/linux/posix


## links for self-study

If you want to know more, see these links:

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


## extra steps for VSCode users

**VSCode** is a short name for an [IDE] called
_Microsoft Visual Studio Code_.

The docs for running Python scripts are here:
```
https://code.visualstudio.com/docs/python/run
```
The docs for creating virtual environments are here:
```
https://code.visualstudio.com/docs/python/environments
```
The docs for deleting virtual environments are here:
```
https://code.visualstudio.com/docs/python/environments#_delete-environments
``

**Caution:** All of these docs are incorrect.


### create a file

- Launch VSCode.
- In the File menu, click `Open folder`.
- Select your project folder. (Mine is `~/code/chengdu`.)
- On the left sidebar, under the word `EXPLORER`, right-click and choose `New file`.
- Enter the name of the file you want to create.
- Press CTRL-S to save the file.

[IDE]: https://github.com/resources/articles/what-is-an-ide


### run a Python script

- Create a file called `hello.py`. Add this to the file:
```
# First program
print("Hello, World!")
```
- Press CTRL-SHIFT-P to open the Command Palette.
- Search for `Python: Select Interpreter` and select it.
- Choose a Python interpreter or press ESC to close the popup.
- Click the ▶ button to run `hello.py`.

### run the Python REPL

**REPL** is Python's _Read-Evaluate-Print-Loop_.
It's what you see when you run `python` or `python3`.
VSCode has its own custom REPL. Here's hot to run it:

- Launch VSCode.
- Press CTRL-SHIFT-P to open the Command Palette.
- Search for `Python: Start Native Python REPL` and select it.
- This should open a new tab called `Python REPL`.
- Enter `2 + 2` and press Enter. It should return 4.

### create a virtual environment

- Create a file called `requirements.txt`.
- Copy everything from [requirements.txt] into that file.
- Create a file called `xiongmao.py`. Add this to the file:
```
# Check if pandas is installed

import pandas as pd

pd.show_versions()
```
- In the far-left sidebar, find the Python logo and click it.
(It looks like the Python logo two cartoon snakes.)
This should open the `Python Environments` view.

**Caution:** My VSCode had no `Python Environments` view.
This is a bug caused by [VSCode issue 581]:
<blockquote>
Note: The Python Environments icon may no longer appear in the Activity Bar due to the ongoing rollout of the Python Environments extension. To restore the extension, add "python.useEnvironmentsExtension": true to your User settings. This setting is temporarily necessary until the rollout is complete!
</blockquote>
Here's the workaround I used:

  - In the `Code` menu, choose `Settings`, then `Settings`.
  - Search for `python.useEnvironmentsExtension`.
  - Click `Enables the Python environments extension.`

**Caution:** My VSCode automatically installed many packages
to my Python installation and broke it. Here's how to undo that:

  - In the second-to-left sidebar, find `ENVIRONMENT MANAGERS`.
  - Find the Python version that VSCode modified.
  - Right click it and select `Delete environment`.
  - Open a Terminal and run this command:
  ```
  pip uninstall -y -r <(pip freeze)
  ```

- Press CTRL-SHIFT-P to open the Command Palette.
- Search for `Python: Create Environment` and select it.
- VSCode should show this prompt:
  ```
  Select an environment manager
  ```
- Choose `venv`.
- VSCode should show this prompt:
  ```
  Select a Python Environment
  ```
  **Caution:** This prompt is a VSCode bug. The options shown
  are Python interpreters, not python environments.
- Choose any recent Python version.
- VSCode should show this prompt:
  ```
  Enter a name for the virtual environment
  ```
- Enter `.venv`.
- VSCode should show a menu. Select this option:
  ```
  Install project dependencies
  ```
  Find your project folder and choose `requirements.txt`.

**Caution:** This menu might not appear if you have created
one or more environment(s), or if VSCode has automatically one or more created environment(s), or if VSCode had automatically detected one or more environments.





[requirements.txt]: requirements.txt
[VSCode issue 581]: https://github.com/microsoft/vscode-python-environments/issues/581



## run jupyter notebooks







