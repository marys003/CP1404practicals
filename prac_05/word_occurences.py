"""
word occurences
Estimate: 30 minutes
Actual:   55 minutes
"""
def main():
    sentence = input("Enter the sentence: ")
    word_to_count = {}
    words = sentence.split()

    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1

    format_word(word_to_count)

def format_word(word_to_count):
    max_word_length = max(len(word) for word in word_to_count)
    for word, count in sorted(word_to_count.items()):
        print(f"{word:>{max_word_length}} : {count}")

if __name__ == "__main__":
    main()

