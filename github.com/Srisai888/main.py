def main():
    path_file = "C:/Users/srisa/Desktop/python/github.com/Srisai888/bookbot/books/frankenstein.txt"
    text = reading_file(path_file)
    words_len = splitting_path(text)
    chars_dict = get_chars_dict(text)
    print(f"{words_len} total number of words")
    print(chars_dict)
    
def reading_file(path):
    with open(path) as f:
        return f.read()

def splitting_path(text):
    words = text.split()
    return len(words) 

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
      
main()    