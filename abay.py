import re
import nltk

# Define function to clean the text
def clean_text(text):
    # Remove unnecessary characters like @%7% but keep letters and spaces
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    return text

# Ask user to input or paste text
input_text = input("Paste your text here: ")

# Clean the text
cleaned_data = clean_text(input_text)

# Print the cleaned text to the console
print("\nCleaned Text:")
print(cleaned_data)
