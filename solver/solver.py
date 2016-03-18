"""
countdown.solver
~~~~~~~~~~~~

This module finds all possible anagrams from a given list of letters.
It checks every possible permutation of the word aginst a dictionary.
A dictionary and a list of letters are given as arguments to the main module.
"""

# 1: dictionary
# preprocessing:
# sort word, add it to dictionary
# add all words to that key
# then when you sort a given word you will instantly have all anagrams
# save as text file and pickle files

# 2: try hashing

# 3: try finding all permutations
# then search each permutation in the dictionary

# 4: try heaps algorithm

# try lab problems

# do gambit worksheet

# init
import pickle
from collections import defaultdict


def load_word_list(filename):
    # Load in word_list (unpickle)
    filename += ".pkl"
    word_list = pickle.load(open(filename, 'rb'))

    return word_list


def save_word_dict(filename, word_dict, serialize=2):
    def pkl_words():
        pkl_filename = filename + '.pkl'
        output = open(pkl_filename, 'wb')
        pickle.dump(word_dict, output)
        output.close()
        print("serialized words to ", pkl_filename)

    def txt_words():
        txt_filename = filename + '.txt'
        file = open(txt_filename, 'w')
        for key, value in word_dict.items():
            file.write('%s\t%s\n' % (key, value))
        file.close()
        print("saved words to ", txt_filename)

    if serialize == 0:
        pkl_words()
    elif serialize == 1:
        txt_words()
    else:
        pkl_words()
        txt_words()


def add_dict_words(word_list):
    word_dict = defaultdict(list)

    for word in word_list:
        srt_word = ''.join(sorted(word))
        word_dict[srt_word].append(word)

    return word_dict


def solver():
    if __name__ == "__main__":
        word_dict_file = 'word_dict'
        word_list_file = "../web_scraper/word_list"
    else:
        word_dict_file = 'solver/word_dict'
        word_list_file = "web_scraper/word_list"

    # load word list
    word_list = load_word_list(word_list_file)

    # go through each word
    word_dict = add_dict_words(word_list)

    # print(word_dict, '\n')

    # save dictionary
    save_word_dict(word_dict_file, word_dict)

    print("%s keys in the word dict.\n" % (len(word_dict)))

def run():
    solver()

if __name__ == "__main__":
    run()