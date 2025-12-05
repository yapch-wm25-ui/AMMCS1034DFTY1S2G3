from myinputreaders import *
from mystringinput import *

def main():
    text = read_string("Enter a string: ")

    print("\n No of word: ", count_words(text))

    print("Average word lenght: {:.2f}\n".format(calculate_average_word_lenght(text)))
          
    for vowel,frequency in count_vowel_aeiou(text).items():
        print("No of {} :{:d}".format(vowel,frequency))

main()