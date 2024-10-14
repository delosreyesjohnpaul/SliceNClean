# Function to count and print the number of characters in the text file
def count_characters(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        character_count = len(text)
    print(f"Total number of characters in '{file_path}': {character_count}")
    return character_count

# Define function to split the text file into chunks and save them
def split_file(file_path, chunk_size, output_prefix):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Calculate the number of chunks
    total_length = len(text)
    num_chunks = (total_length // chunk_size) + (1 if total_length % chunk_size != 0 else 0)

    for i in range(num_chunks):
        # Create a chunk of the specified size
        chunk = text[i * chunk_size:(i + 1) * chunk_size]

        # Save the chunk into a new text file
        output_file = f'{output_prefix}_chunk_{i + 1}.txt'
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(chunk)
        print(f"Saved {output_file}")

# Parameters
file_path = 'sample.txt'  # Path to your input file
chunk_size = 10000  # Chunk size in characters
output_prefix = 'sample_Text'  # Prefix for output files

# Count characters before splitting
count_characters(file_path)

# Run the function to split the file
split_file(file_path, chunk_size, output_prefix)
