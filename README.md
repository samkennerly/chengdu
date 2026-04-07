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
the path will start with `C:` or `D:` or something like that.
For example, it might look like this:
```
C:\Users\Lenovo\Projects\Chengdu
```
If you have `git` installed, then you can [clone] this repo.

[clone]: https://git-scm.com/docs/git-clone


## install dependencies

The `mkvenv` file is a [shell script] that creates a
[virtual environment] and installs required packages.
On any [POSIX] operating system (Linux, BSD, macOS, 麒麟, etc.),
you can run it by entering this command in a terminal:
```
./mkvenv
```
If you use Windows, or you want to know what the script does,
open the file in a text editor and run the commands yourself.

**Caution:** On my computer, the command to run Python 3 is `python3`. On some computers, it's `python` without the `3`.

[virtual environment]: https://docs.python.org/3/library/venv.html
[shell script]: https://www.dotlinux.net/linux-shell-scripting-tutorial/
[POSIX]: https://www.baeldung.com/linux/posix


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
```

[IDE]: https://github.com/resources/articles/what-is-an-ide

### create a file

- Launch VSCode.
- In the File menu, click `Open folder`.
- Select your project folder. (Mine is `~/code/chengdu`.)
- On the left sidebar, under the word `EXPLORER`, right-click and choose `New file`.
- Enter the name of the file you want to create.
- Press CTRL-S to save the file.

### run a Python script

- Create a file named `hello.py`. Add this to the file:
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

- Create a file named `requirements.txt`.
- Copy everything from [requirements.txt] into that file.
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

**Caution:** My VSCode automatically installed packages to my
my clean Python environment and broke it. Here's how I fixed it:

  - In the second-to-left sidebar, find `ENVIRONMENT MANAGERS`.
  - Find the Python version that VSCode modified.
  - Right click it and select `Delete environment`.
  - Open a Terminal and run this command:
```
pip uninstall -y -r <(pip freeze)
```

If you can see the `Python Environments` view,

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
- The options VSCode shows are Python versions, not python environments. Choose any recent Python version.
- VSCode should show this prompt:
```
Enter a name for the virtual environment
```
- Enter `.venv`.
- VSCode should show a popup. Select this option:
```
Install project dependencies
```
- VSCode should show a popup. Select this option:
```
requirements.txt
```
- Wait for VSCode to install packages.

[requirements.txt]: requirements.txt
[VSCode issue 581]: https://github.com/microsoft/vscode-python-environments/issues/581

## choose a Python environment

When you run a script, VSCode automatically decides which Python environment to use. When it's wrong, this is how I fix it:

- In the bottom-right corner of the VSCode window, look for some text like this:
```
Python .venv (3.14.2)
```

**Caution:** VSCode automatically removed this on my machine.
To fix it, right-click on any empty space in the `Status Bar`
(it's the bar at the far bottom of the screen)
and click `Python interpreter`.

- Click on the version number (Mine is `3.14.2`. Yours might be different) to open a popup. Select the environment you want.


## run jupyter notebooks

- On the far-left of the VSCode window, find the `EXTENSIONS` view. (It's the icon that looks like four squares.)

**Caution:** Do not click `Install`. By default, VSCode installs a recent Jupyter extension which does not work.

- Search for `Jupyter` and right-click it.
- Chose `Install specific version.`
- Search for `2025.4.1` and select it.
- Wait for VSCode to install its Jupyter extension.
- On the far-left of the VSCode window, find the `EXPLORER` view. (It's the icon that looks like sheets of paper.)
- Create a file named `hello.ipynb`.
- In the `hello.ipynb` tab, click `+ Code` to add a new cell.
- Enter this code:
```
import pandas as pd

pd.show_versions()
```
- Click the `▶ RunAll` button.
- A popup should appear with this prompt:
```
Select kernel for 'hello.ipynb'
```
- Choose `.venv`.
- You should see this under the cell:
If it worked, you should see seomthing like this in the terminal:
```
INSTALLED VERSIONS
------------------
commit                : ab90747e3dae0e69b1bdbf083820b8075689b34b
python                : 3.14.2
python-bits           : 64
OS                    : Darwin
OS-release            : 24.6.0
Version               : Darwin Kernel Version 24.6.0: Mon Jan 19 22:01:13 PST 2026; root:xnu-11417.140.69.708.3~1/RELEASE_ARM64_T8122
machine               : arm64
processor             : arm
byteorder             : little
LC_ALL                : None
LANG                  : en_US.UTF-8
LOCALE                : en_US.UTF-8

pandas                : 3.0.2
numpy                 : 2.4.4
...
```
The output will be different on different machines. That's OK!
The most important thing is: you have `pandas`.


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
