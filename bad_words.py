import urllib

def read_text():
    quotes = open("/Users/benjamindunisch/Desktop/Udacity/movie_quotes.txt")
    content_of_file = quotes.read()
    check_bad_words(content_of_file)
    quotes.close()

def check_bad_words(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    if output == "true":
        print("You used bad words")
    else:
        print("You used just good words")
    connection.close()
    
read_text()
