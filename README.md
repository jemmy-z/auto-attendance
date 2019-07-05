# auto-attendance

## Set-up
- To use this form, you must install [Selenium](https://selenium-python.readthedocs.io/index.html). You can do that by running `pip install selenium`.

## Requirements
- The form must be a Google Form. There can only be only short-text input blank. **More options coming soon!**
- You must have Chrome v75 installed.
- The emails in the .csv file must be in the first column, one email per row.

## Instructions
To auto-upload your attendance, run `python3 upload.py <form url> <\~path~\attendance.csv>`.
