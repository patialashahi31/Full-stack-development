
import urllib.request







def read_from_file():
    quotes = open("quotes.txt")
    contents = quotes.read()
    print(contents)
    profanity(contents)
    quotes.close()


def profanity(text):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    output = connection.read()
    print(output)
    connection.close()


read_from_file()