# chengdu


This [git repo] contains example code and data for class.

The **builtin** folder contains Python scripts.
These use Python's [builtin] functions and libraries.

The **science** folder contains [Jupyter notebooks].
Required Python [packages] are in `requirements.txt`.

The **science/data** folder contains example datasets.
Use these for class projects or find your own datasets.

The **science/projects** folder contains example projects.
Read these for class project ideas or create your own.

[git repo]: https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#ch02-git-basics-chapter
[builtin]: https://docs.python.org/3/library/index.html
[Jupyter notebooks]: https://jupyter-notebook.readthedocs.io/
[packages]: https://packaging.python.org/


## choose a project folder

Create a folder (also known as a _directory_) for this repo.
Name it whatever you want. For example, mine is:
```
~/code/chengdu/
```
On Windows, the `/` slashes will be `\` backslashes,
and the path will start with a drive letter like `C:` or `D:`.
For example, it might look like this:
```
C:\Users\Lenovo\Projects\Chengdu
```
If you have `git` installed, then you can [git clone] this repo
and [git pull] to get the latest changes.

[git clone]: https://git-scm.com/docs/git-clone
[git pull]: https://git-scm.com/docs/git-pull


## how to use this repo (without VSCode)

The `mkvenv` file is a [shell script] that creates a
[virtual environment] and installs required packages.
On any [POSIX] operating system (Linux, BSD, macOS, 麒麟, etc.),
you can run it by opening a terminal and running this command:
```
./mkvenv
```

**Caution:** On some computers, the command to run Python 3 is
`python`, not `python3`.

To activate the virtual environment, run this:
```
source .venv/bin/activate
```

You should see `(.venv)` next to your prompt.
For example, mine looks like this:
```
(.venv) sam@hal9001 ~/code/chengdu
```

To launch a [Jupyter server], run this:
```
jupyter notebook
```

Follow the instructions on screen. (On some computers, you don't need to do anything. Jupyter opens itself in a browser.)
In your browser, click `New` and choose `Python 3 (ipykernel)`.
Type this code and click the `▶` button:
```
import pandas as pd

pd.show_versions()
```

To stop Jupyter, click on the terminal and press CTRL-C.
You should see this prompt:
```
Shut down this Jupyter server (y/[n])?
```

Enter `y`. To deactivate the environment, run:
```
deactivate
```

[virtual environment]: https://docs.python.org/3/library/venv.html
[shell script]: https://www.dotlinux.net/linux-shell-scripting-tutorial/
[POSIX]: https://www.baeldung.com/linux/posix
[Jupyter server]: https://jupyter-server.readthedocs.io/en/latest/index.html


## how to use this repo (with VSCode)

**VSCode** is a short name for an [IDE] called
_Microsoft Visual Studio Code_.

Here are some of the official VSCode docs:

- run Python scripts
https://code.visualstudio.com/docs/python/run

- create virtual environments
https://code.visualstudio.com/docs/python/environments

- delete virtual environments
https://code.visualstudio.com/docs/python/environments#_delete-environments

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
Here's how to run it in VSCode:

- Launch VSCode.
- Press CTRL-SHIFT-P to open the Command Palette.
- Search for `Python: Start Native Python REPL` and select it.
- This should open a new tab called `Python REPL`.
- Enter `2 + 2` and press Enter. It should return 4.

### create a virtual environment

- Create a file named `requirements.txt`.
- Copy everything from [requirements.txt] into that file.
- In the far-left sidebar, find the Python logo and click it.
(It looks like two cartoon snakes.)
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

**Caution:** VSCode automatically installed packages to my clean Python environment. Here's how I removed them:

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

- Choose `venv`. VSCode should show this prompt:
```
Select a Python Environment
```

- The options VSCode shows are Python versions,
not python environments. Choose any recent Python version.
VSCode should show this prompt:
```
Enter a name for the virtual environment
```

- Enter `.venv`. VSCode should show a popup. Select this:
```
Install project dependencies
```

- VSCode should show a popup. Select this:
```
requirements.txt
```

- Wait for VSCode to install packages.


### choose a Python environment

VSCode automatically decides which Python environment to use. When it's wrong, this is how I fix it:

- In the bottom-right corner of the VSCode window, look for some text like this:
```
Python .venv (3.14.2)
```

- Click on the version number (Mine is `3.14.2`. Yours might be different.) to open a popup.

- Select the environment you want to use.

**Caution:** VSCode automatically removed this on my machine.
To fix it, right-click on any empty space in the `Status Bar`
(the bar at the far bottom of the screen)
and click `Python interpreter`.


### run jupyter notebooks

- On the far-left of the VSCode window, find the `EXTENSIONS` view. (It's the icon that looks like four squares.)

**Caution:** Do not click `Install`. VSCode will automatically install a Jupyter extension which does not work.
See [VSCode issue 17042] for details.

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

- Click the `▶ RunAll` button. A popup should appear with this prompt:
```
Select kernel for 'hello.ipynb'
```

- Choose `.venv`. If it runs, and you see output, then you have pandas.

[IDE]: https://github.com/resources/articles/what-is-an-ide
[requirements.txt]: requirements.txt
[VSCode issue 581]: https://github.com/microsoft/vscode-python-environments/issues/581
[VSCode issue 17042]: https://github.com/microsoft/vscode-jupyter/issues/17042


## links for self-study

If you want to know more, see these links:

- class textbook
https://automatetheboringstuff.com/
- python docs in 中文
https://docs.python.org/zh-cn/3/
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
https://scikit-learn.org/
