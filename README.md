# Book Store Application

A simple command-line book manager built with Python.

## Features

- Add new books
- Search for books by keyword
- Display the full list of books
- Save books to a text file
- Load saved books when the program starts

## How It Works

The application stores books with the following information:

- Book name
- Author name
- Number of pages

When the program starts, it tries to load existing books from `theBooksList.txt`.

If the file does not exist, the program starts with an empty book list.

When the program closes, the current book list is saved back to `theBooksList.txt`.

## How to Run

```bash
python main.py
```

## Purpose

This project was built as part of my software engineering learning journey.

The goal was to practice:

- Python basics
- File reading and writing
- User input
- Simple search logic
- Git and GitHub workflow

## Lessons Learned

- Working with lists and nested data
- Reading and writing files in Python
- Handling user interaction in the terminal
- Structuring a simple CLI application