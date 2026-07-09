# How to Submit an Assignment

Follow this process for every assignment. Create one branch and one Pull Request for one assignment day only.

## 1. Clone the Repository

```bash
git clone https://github.com/z-pandeyji/BIT-SummerTraining.git
cd BIT-SummerTraining
```

## 2. Start From the Latest Main Branch

Always start a new assignment from `main`:

```bash
git checkout main
git pull origin main
git checkout -b day-06-your-name
```

Example:

```bash
git checkout -b day-06-rahul
```

Do not create a Day 6 branch from your Day 5 branch. That causes old files to appear in the new Pull Request.

## 3. Create Only Your Submission Files

Choose your batch and create one folder using your own name.

```txt
assignments/day-06/submissions/batch-a/your-name/solution.py
```

or

```txt
assignments/day-06/submissions/batch-b/your-name/solution.py
```

Example:

```txt
assignments/day-06/submissions/batch-a/rahul/solution.py
```

Most assignments need only `solution.py`. If an assignment specifically asks for a data file, such as Day 7, keep that file inside your own folder too:

```txt
assignments/day-07/submissions/batch-a/rahul/solution.py
assignments/day-07/submissions/batch-a/rahul/sales_data.csv
```

## 4. Run Your Program

Run the file before committing it:

```bash
python3 assignments/day-06/submissions/batch-a/your-name/solution.py
```

Check that every required question runs and that printed values match the expected output in `questions.md`.

## 5. Stage Only Your Files

Do not use `git add .`. Stage only your own submission files.

```bash
git add assignments/day-06/submissions/batch-a/your-name/solution.py
git commit -m "Add Day 6 assignment by Your Name"
git push origin day-06-your-name
```

For Day 7, stage both files:

```bash
git add assignments/day-07/submissions/batch-a/your-name/solution.py
git add assignments/day-07/submissions/batch-a/your-name/sales_data.csv
git commit -m "Add Day 7 assignment by Your Name"
git push origin day-07-your-name
```

## 6. Create the Pull Request

On GitHub, create a Pull Request from your branch to `main`.

Use this title format:

```txt
Day 6 Assignment - Rahul
```

## Before You Create the Pull Request

Run this command:

```bash
git status --short
```

The output should show only files inside your own submission folder for one assignment day.

Do not include:

- Another student's folder or solution file.
- Files from an earlier or later assignment day.
- `README.md`, `CONTRIBUTING.md`, `.gitignore`, or `questions.md`.
- `resources/`, generated files, temporary files, or editor backup files.

## If Your Pull Request Contains Wrong Files

Create a clean branch instead of adding more files to the old branch:

```bash
git checkout main
git pull origin main
git checkout -b day-06-your-name-clean
```

Copy only your correct `solution.py` into the required folder, commit it, push it, and create a new Pull Request.
