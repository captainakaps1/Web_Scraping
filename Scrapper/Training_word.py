from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.nobleprog.co.uk').text
count = 0

list_of_words_by_space = html_text.split(" ")
list_of_words_by_dash = html_text.split("-")
words = list_of_words_by_dash + list_of_words_by_space

for word in words:
    word = word.lower()

for word in words:
    if word == "training":
        count = count + 1


print(count)
