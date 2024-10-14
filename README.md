# SliceNClean

SliceNClean is a Python project designed to clean and chunk text files. The main functionality of this project is to remove unnecessary characters, convert text to lowercase, and remove stopwords from the text files.

## Overview

This project provides a simple and efficient way to preprocess text data. It reads raw text files, cleans the content by removing unwanted characters and stopwords, and then saves the cleaned data to new text files. This preprocessing step is essential for various natural language processing (NLP) tasks.

## Installation

To use this project, you need to have Python installed on your system. Additionally, you need to install the `nltk` library, which can be done using pip:

```bash
pip install nltk
```

## Usage

1. Place your raw text files in the `RawData` directory.
2. Run the `datacleaner.py` script to clean the text files.

Example command to run the script:

```bash
python datacleaner.py
```

## Code Example

Here is an example of how the code works:

```python
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')

# Define function to clean the text
def clean_text(text):
    # Remove unnecessary characters like @%7%
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    
    return text

# Load the input text file
input_file_path = 'RawData/Solar Powered Feeder for Pet Fish and Management System.txt'
output_file_path = 'CleanedData/Solar Powered Feeder for Pet Fish and Management System.txt'

with open(input_file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# Clean the text
cleaned_data = clean_text(data)

# Save cleaned data to a new text file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(cleaned_data)

print(f"Cleaned text saved to {output_file_path}")
```

## License

This project is licensed under the MIT License.
