import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

restaurant_list = soup.find_all('div', {'class': 'lemon--div__373c0__1mboc searchResult__373c0__1yggB border-color--default__373c0__2oFDT'})

data = []

for restaurant in restaurant_list:
    name = restaurant.find('a', {'class': 'lemon--a__373c0__IEZFH link__373c0__29943 link-color--inherit__373c0__15ymx'}).text.strip()
    rating = restaurant.find('div', {'class': 'lemon--div__373c0__1mboc i-stars__373c0__30xVZ'})['aria-label'].strip()
    review_count = restaurant.find('span', {'class': 'lemon--span__373c0__3997G text__373c0__2Kxyz reviewCount__373c0__2r4xT text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-'}).text.strip()
    address = restaurant.find('span', {'class': 'lemon--span__373c0__3997G raw__373c0__3rcx7'}).text.strip()
    data.append([name, rating, review_count, address])

df = pd.DataFrame(data, columns=['Name', 'Rating', 'Review Count', 'Address'])

print(df.head())
