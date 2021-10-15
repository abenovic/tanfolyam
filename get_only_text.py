from bs4 import BeautifulSoup
from requests import get

content = get("https://index.hu").text
soup = BeautifulSoup(content)
only_text = soup.get_text()
lines = only_text.splitlines()
for line in lines:
    if len(line.strip()) != 0:
        print(line)