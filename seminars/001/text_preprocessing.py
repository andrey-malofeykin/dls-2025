import nltk
from nltk import sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

def main():

    data = "All work and no play makes jack a dull boy, all work and no play"

    tokens = word_tokenize(data.lower())
    print(tokens)

    print(sent_tokenize("I was going home when she rung. It was a surprise"))


if __name__ == '__main__':
    main()