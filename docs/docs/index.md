# My Project Documentation

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
  - [process_file](#process_file)
  - [count_words](#count_words)
  - [extract_images_from_docx](#extract_images_from_docx)
- [License](#license)

---

## Introduction

This project provides a set of utility functions for processing text and DOCX files. It allows users to read text files, extract text from DOCX documents, count words in a given text, and extract images from DOCX files.

## Installation

To use this project, ensure you have Python installed. You can install the necessary dependencies using pip. Create a `requirements.txt` file and include the following:

## Add your project dependencies here

Then, install the dependencies:

```bash
pip install -r requirements.txt
``` 

## Usage
You can use the functions provided in this project as follows:

### Process a file (supports .txt and .docx formats):

```python
content = process_file('path/to/your/file.txt')  # for text files
content = process_file('path/to/your/file.docx')  # for DOCX files
print(content)
```

### Count words in a given text:

```python
text = "This is an example text."
word_count = count_words(text)
print(f"Number of words: {word_count}")
```

### Extract images from a DOCX file:

```python
image_count = extract_images_from_docx('path/to/your/file.docx')
print(f"Number of images extracted: {image_count}")
```

## Functions

### process_file
Reads the content of a file. Supports .txt and .docx formats.
- Parameters:
  - file_path (str): Path to the file to be processed.
- Output: 
  - str: Content of the file.
- Raises: 
  - ValueError: If the file format is unsupported.

### count_words 
Counts the number of words in a given text.
- Parameters:
  - text (str): The text to count words from.
- Output: 
  - int: Number of words in the text.

### extract_images_from_docx
Extracts images from a DOCX file and saves them in the specified directory.
- Parameters:
  - file_path (str): Path to the DOCX file.
- Output: 
  - int: Number of images extracted.

## License
This project is licensed under the MIT License. See the LICENSE file for details.