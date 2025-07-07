from google_play_scraper import reviews_all, Sort
import pandas as pd

def scraping():
    print("Sedang melakukan scraping...")
    reviews = reviews_all(
        'id.dana',
        lang='id',
        country='id',
        sort=Sort.MOST_RELEVANT,
        count=15000
    )
    
    df = pd.DataFrame(reviews)
    df.to_csv('dataset.csv', index=False, encoding='utf-8')

if __name__ == "__main__":
    scraping()