import requests
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
from transformers import pipeline  

sentiment_analyzer = pipeline('sentiment-analysis')

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').text.strip()
        author = quote.find('small', class_='author').text.strip()
        sentiment = sentiment_analyzer(text)[0]  # Get sentiment
        data.append({'quote': text, 'author': author, 'sentiment': sentiment['label']})
    
    return data

base_url = 'https://quotes.toscrape.com/page/'

data = []
page = 1

while page <= 5:
    url = f"{base_url}{page}/"
    data.extend(scrape_page(url))
    page += 1

df = pd.DataFrame(data)

# Step 4: Store into MySQL with sentiment
db = mysql.connector.connect(
    host='localhost',
    user='root',           
    password='root123',    
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS chatbot_db")
cursor.execute("USE chatbot_db")
cursor.execute("CREATE TABLE IF NOT EXISTS quotes (id INT AUTO_INCREMENT PRIMARY KEY, quote TEXT, author VARCHAR(255), sentiment VARCHAR(50))")


for _, row in df.iterrows():
    cursor.execute("INSERT INTO quotes (quote, author, sentiment) VALUES (%s, %s, %s)", 
                   (row['quote'], row['author'], row['sentiment']))
db.commit()
db.close()

print("Data loaded into MySQL successfully.")

