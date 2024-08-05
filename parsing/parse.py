# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://yandex.uz/pogoda/tashkent?lat=41.311151&lon=69.279737'
# response = requests.get(url)
# html_content = response.content
#
#
# soup = BeautifulSoup(html_content, 'html.parser')
#
# element = soup.find_all('span', class_='temp__pre')
#
# print(element)

# headers = soup.find_all('h1')
# print('Заголовки (h1):')
# for header in headers:
#     print(header.text)
#
# # links = soup.select('a')
# print('\nСсылки')
# for link in links:
#     print(link.get('href'))