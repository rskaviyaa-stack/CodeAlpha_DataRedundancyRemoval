# CodeAlpha Data Redundancy Removal System

## Overview
This beginner-friendly Python project helps prevent duplicate records from being saved. It checks each email address before adding a record and stores accepted records in a local JSON file.

## Features
- Validates that a name and email address are provided.
- Checks email addresses without case sensitivity and ignores extra spaces.
- Prevents duplicate email addresses from being added.
- Saves accepted records in `database.json`.
- Lets users add and view records through a simple menu.

## Requirements
- Python 3.8 or later
- No additional packages are required.

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python Main.py
   ```

   On some systems, use `python3 Main.py`.

## Example test
1. Choose `1` and enter `Kavya` and `kavya@example.com`.
2. Choose `1` again and enter `Kavya S` and `KAVYA@example.com`.
3. The second entry should be rejected as a duplicate.
4. Choose `2` to view the saved records.

## Project files
- `Main.py` — program source code
- `README.md` — project documentation
- `output.txt` — sample run for reference

## Note
This is a learning/demo project using a local JSON file, not a production cloud database. For a real cloud deployment, connect it to a database service and add authentication, authorization, backups, and secure configuration.
