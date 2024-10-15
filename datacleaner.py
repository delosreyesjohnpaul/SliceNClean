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
input_file_path = 'RawData/D21.txt'
output_file_path = 'CleanedData/D21.txt'

with open(input_file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# Clean the text
cleaned_data = clean_text(data)

# Save cleaned data to a new text file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(cleaned_data)

print(f"Cleaned text saved to {output_file_path}")
