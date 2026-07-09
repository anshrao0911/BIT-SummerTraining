# Setup Guide

Use this guide to prepare your system for Python assignments and GitHub submissions.

## Install Python

Download and install Python from:

```txt
https://www.python.org/downloads/
```

After installation, check Python:

```bash
python --version
```

or

```bash
python3 --version
```

## Install VS Code

Download and install Visual Studio Code:

```txt
https://code.visualstudio.com/
```

Recommended VS Code extensions:

- Python
- Jupyter
- GitHub Pull Requests

## Install Git

Download and install Git:

```txt
https://git-scm.com/downloads
```

Check Git:

```bash
git --version
```

## Configure Git

Run these commands once:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

## Basic GitHub Assignment Flow

```bash
git clone <repo-link>
cd BIT-SummerTraining
git checkout -b day-01-your-name
git add .
git commit -m "Day 1 assignment by Your Name"
git push origin day-01-your-name
```

Then create a Pull Request on GitHub.
