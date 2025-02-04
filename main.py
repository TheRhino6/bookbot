def main():
    book_path = "books/frankenstein.txt"
    #text = get_book_text(book_path)
    #print(text)
    amount = count_characters(book_path)
    #print(amount)
    number = count_ind_characters(book_path)
    #print(number)
    report = generate_report(amount, number)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_characters(path):
    with open(path) as f:
        words = len(f.read().split())
        return words

def count_ind_characters(path):
    dic = {}
    char = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "!", ",", ".", "?", ";", ":", "(", ")", "-", "_", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    with open(path) as f:
        string = f.read()
        lowered_string = string.lower()
    
    for c in char:
        dic[c] = lowered_string.count(c)

    return dic

def generate_report(amount, number):
    print ("---Begin report of books/frankenstein.txt ---")
    print (f"{amount} words found in the document")
    print (" ")

    letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for l in letter:
        print(f"The '{l}' character was found {number[l]} times")

    print ("--- End report ---")

main()
