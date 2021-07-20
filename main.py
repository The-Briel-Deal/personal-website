from bs4 import BeautifulSoup
with open('index.html', mode='r') as webpage:
    contents = webpage.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.find_all(name='td'))
