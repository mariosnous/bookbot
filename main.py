def main():
    book_path = "github.com/username/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document \n")

    letter_counts = count_letters(text)
    sorted_letter_counts = sorted(letter_counts.items(), key=sort_by_appearances, reverse=True)

    for char, count in sorted_letter_counts:
        print(f"The '{char}' character was found: {count} times")

    print("\n--- End of Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    count_letters_dict = {}
    for char in text:
        if char.isalpha():
            if char in count_letters_dict:
                count_letters_dict[char] += 1
            else:
                count_letters_dict[char] = 1
    return count_letters_dict

def sort_by_appearances(item):
    return item[1]

if __name__ == "__main__":
    main()
