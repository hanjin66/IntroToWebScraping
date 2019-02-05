import requests
from bs4 import BeautifulSoup
import re



r = requests.get('https://sageelliott.com/scrape/')

# print(r.content)


c = r.content
soup = BeautifulSoup(c, 'lxml')

# print(soup)

# print(soup.prettify())



main_content = soup.find('div', attrs = {'class': 'main-content'})
# print(main_content)


list_content = soup.find('div', attrs = {'class': 'main-content'}).ul
# print(list_content)

list_text_content = main_content.find('ul').text

print(list_text_content)

content = main_content.find('h2').text

print(content)

content = main_content.find_all('h2')
for h2 in content:
    print(h2.text)

content = main_content.find_all('a')

for link in content:
    print(link.text+":")
    print(link['href'])
   
salary_pattern = re.compile(r'\$.+')
salaries = salary_pattern.findall(list_text_content)

print(salaries)