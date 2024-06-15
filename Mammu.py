import os

def count_word_frequencies(file_path):
    """Reads a text file and counts occurrences of each word, displaying them in descending order."""
    word_counts = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Remove punctuation and convert to lowercase
                line = line.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')).lower()
                words = line.split()
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
    except FileNotFoundError:
        print("The file was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Sort words by frequency in descending order and print them
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

def main():
    # Absolute path to the text file
    directory_path = r"C:\Users\M.Jayanthi\OneDrive\Desktop\python"
    file_name = "sample.txt"
    file_path = os.path.join(directory_path, file_name)

    # Count word frequencies and display results
    count_word_frequencies(file_path)

if __name__ == "__main__":
    main()
