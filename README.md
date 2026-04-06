# chengdu


## choose a project folder

First, decide where you want to save this project.
Create a folder (also known as a _directory_) on your computer.
Add a subfolder (also known as a _subdirectory_) called `builtin`.
For example, mine is:
```
~/code/chengdu/builtin
```
On Windows, the `/` (slashes) will be `\` (backslashes),
and the path will start with `C:` or `D:` or something similar.
For example, it might look any of these:
```
C:\Users\lenovo\projects\builtin
```


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
