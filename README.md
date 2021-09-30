# tkinter_collection

Collection of simple gui parts using tkinter - might come in handy for building simple python projects at the Uni level

## Freezing your project requirements

- use `pip freeze > requirements.txt` in order to freeze current state of imports into requirements.txt
- otherwise, use `pip freeze >> requirements.txt` to append to existing requirements.txt file

## Create new virtual env (WSL)

- run `virtualenv <folder>`
- activate: `. <folder>/bin/activate`

## Using Virtual Env:

To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:

```
python3 -m venv tutorial-env
```

This will create the tutorial-env directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter, the standard library, and various supporting files.

A common directory location for a virtual environment is `.venv`. This name keeps the directory typically hidden in your shell and thus out of the way while giving it a name that explains why the directory exists. It also prevents clashing with .env environment variable definition files that some tooling supports.

Once you’ve created a virtual environment, you may activate it.

On Windows, run: (do this in cmd rather than powershell)

```
.\.venv\Scripts\activate.bat
```

On Unix or MacOS, run:

```
source .venv/bin/activate
```
