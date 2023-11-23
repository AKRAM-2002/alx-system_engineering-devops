# 0x04. Loops, Conditions, and Parsing

## DevOps - Shell - Bash Scripting

## Background Context

### Resources
Read or watch:
- [Loops sample](#)
- [Variable assignment and arithmetic](#)
- [Comparison operators](#)
- [File test operators](#)
- [Make your scripts portable](#)
man or help:
- `env`
- `cut`
- `for`
- `while`
- `until`
- `if`

### Learning Objectives
By the end of this project, you should be able to explain the following without using Google:
- How to create SSH keys
- The advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
- How to use `while`, `until`, and `for` loops
- How to use `if`, `else`, `elif`, and `case` condition statements
- How to use the `cut` command
- Understanding file and other comparison operators and how to use them

## Requirements
### General
- Allowed editors: vi, vim, emacs
- Interpretation on Ubuntu 20.04 LTS
- Files should end with a new line
- `README.md` file at the root is mandatory
- All Bash script files must be executable
- Not allowed to use `awk`
- Bash script must pass Shellcheck (version 0.7.0) without errors
- First line of all Bash scripts: `#!/usr/bin/env bash`
- Second line of all Bash scripts: Comment explaining the script's purpose

### Copyright - Plagiarism
- Solutions should be original; no copying or pasting
- No publishing of project content
- Plagiarism is strictly forbidden

### Shellcheck
- Tool for writing proper Bash scripts
- Must pass Shellcheck without errors

## Tasks

### 0. Create a SSH RSA key pair
- Read for this task: [Linux and Mac OS users](#), [Windows users](#), `man: ssh-keygen`
- Requirements:
  - Share public key in `0-RSA_public_key.pub`
  - Fill SSH public key field in intranet profile with generated public key
  - Keep private key secure
  - If passphrase added, save it securely

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x04-loops_conditions_and_parsing)

### 1. For Best School loop
- Write a Bash script displaying "Best School" 10 times.
- Requirements:
  - Use `for` loop (while and until forbidden)

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x04-loops_conditions_and_parsing)

### 2. While Best School loop
- Write a Bash script displaying "Best School" 10 times.
- Requirements:
  - Use `while` loop (for and until forbidden)

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x04-loops_conditions_and_parsing)

### 3. Until Best School loop
- Write a Bash script displaying "Best School" 10 times.
- Requirements:
  - Use `until` loop (for and while forbidden)

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x04-loops_conditions_and_parsing)

### 4. If 9, say Hi!
- Write a Bash script displaying "Best School" 10 times.
- For the 9th iteration, display "Best School" and then "Hi" on a new line.
- Requirements:
  - Use `while` loop (for and until forbidden)
  - Use `if` statement

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x04-loops_conditions_and_parsing)

### 5. 4 bad luck, 8 is your chance
- Write a Bash script that loops from 1 to 10:
  - Display "bad luck" for the 4th iteration
  - Display "good luck" for the 8th iteration
  - Display "Best School" for other iterations
- Requirements:
  - Use `while` loop (for and until forbidden)
  - Use `if`, `elif`, and `else` statements

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x04-loops_conditions_and_parsing)

### 6. Superstitious numbers
- Write a Bash script displaying numbers from 1 to 20:
  - Display "4" and then "bad luck from China" for the 4th iteration
  - Display "9" and then "bad luck from Japan" for the 9th iteration
  - Display "17" and then "bad luck from Italy" for the 17th iteration
- Requirements:
  - Use `while` loop (for and until forbidden)
  - Use `case` statement

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x04-loops_conditions_and_parsing)

### 7. Clock
- Write a Bash script displaying the time for 12 hours and 59 minutes.
- Display hours from 0 to 12 and minutes from 1 to 59.
- Requirements:
  - Use `while` loop (for and until forbidden)

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x04-loops_conditions_and_parsing)

### 8. For ls
- Write a Bash script displaying the content of the current directory in list format.
- Only display the part of the name after the first dash.
- Requirements:
  - Use `for` loop (while and until forbidden)
  - Do not display hidden files

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x04-loops_conditions_and_parsing)

### 9. To file, or not to file
- Write a Bash script giving information about the school file.
- Requirements:
  - Use `if` and `else` (case is forbidden)
  - Check if the file exists and print appropriate messages
  - If the file exists, print additional information about the file

**Repo:**
- [GitHub repository](https://github.com/alx-system_engineering-devops/0x04-loops_conditions_and_parsing)

