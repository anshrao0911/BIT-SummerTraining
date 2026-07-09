# How to Submit Assignment

Follow these steps carefully for every assignment.

## Step 1: Clone Repository

```bash
git clone <repo-link>
cd BIT-SummerTraining
```

## Step 2: Create Branch

Use the day number and your name:

```bash
git checkout -b day-01-your-name
```

Example:

```bash
git checkout -b day-01-rahul
```

## Step 3: Add Your Solution

Create your folder inside your batch:

```txt
assignments/day-01/submissions/batch-a/your-name/
```

or

```txt
assignments/day-01/submissions/batch-b/your-name/
```

Add your file:

```txt
solution.py
```

Final example:

```txt
assignments/day-01/submissions/batch-a/rahul/solution.py
```

## Step 4: Commit

```bash
git add .
git commit -m "Day 1 assignment by Your Name"
```

## Step 5: Push

```bash
git push origin day-01-your-name
```

## Step 6: Create Pull Request

Open GitHub and create a Pull Request from your branch to the main branch.

## Pull Request Rules

Before creating a Pull Request, check:

- Your file is inside the correct day folder.
- Your file is inside your correct batch folder.
- Your folder name is your own name.
- You did not edit another student's files.
- Your code runs without errors.
- Your Pull Request title includes the day number and your name.

Good PR title:

```txt
Day 1 Assignment - Rahul
```
