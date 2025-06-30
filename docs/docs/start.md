# Getting Started
## Installation Guide
### Prerequisites
- Make sure Python and pip are installed in your system (this project use `Python 3.10.3` and `pip 25.1.1`)
- You can check whether your system has Python and pip installed or not.
```bash
# Checking installed Python version.
$ python3 --version

# Checking installed pip version.
$ pip --version
```
- If you haven't install Python or pip, you can use the command below to install them.
```bash
# Installing the latest-version Python.
$ sudo apt install python3

# Installing the latest-version pip.
$ sudo apt install python3-pip

# You can also install venv module.
$ sudo apt install python3-venv
```
- You can create virtual environment using module `venv` from Python. **Make sure you already install the `venv` module**.
```bash
# Creating virtual environment.
$ python3 -m venv your_venv_name

# Activating the virtual environment.
$ source your_venv_name/bin/activate

# Your virtual environment has been activated.
(your_venv_name) $
```

### Installing Packages
- Install the required packages from `requirements.txt` file (you may use virtual environment for this).
```bash
(your_venv_name) $ pip install -r requirements.txt
``` 