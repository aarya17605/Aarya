def count_words_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()
    
        words = text.split()
        word_count = len(words)
        with open(output_file, 'w') as file:
            file.write(f"Number of words: {word_count}\n")
        
        print(f"Word count has been written to {output_file}")
    
    except FileNotFoundError:
        print(f"The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_filename = input("Enter the name of the input text file: ")
output_filename = input("Enter the name of the output file: ")

count_words_in_file(input_filename, output_filename)
