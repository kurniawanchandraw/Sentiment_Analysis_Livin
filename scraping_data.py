
from google_play_scraper import reviews_all, Sort
import csv

def scrape_reviews(app_id: str, lang: str = 'id', country: str = 'id', count: int = 1000) -> list:
    """
    Mengambil ulasan aplikasi dari Google Play Store menggunakan app_id.
    
    Args:
        app_id (str): ID aplikasi yang ingin diambil ulasannya.
        lang (str): Bahasa ulasan yang diinginkan (default 'id' untuk Bahasa Indonesia).
        country (str): Negara asal ulasan yang diinginkan (default 'id' untuk Indonesia).
        count (int): Jumlah ulasan yang ingin diambil (default 1000).
    
    Returns:
        list: Daftar ulasan aplikasi.
    """

    reviews = reviews_all(
        app_id,             # ID aplikasi
        lang=lang,          # Bahasa ulasan
        country=country,    # Negara asal ulasan
        sort=Sort.MOST_RELEVANT, # Urutan ulasan berdasarkan relevansi
        count=count         # Jumlah maksimal ulasan yang diambil
    )
    
    return reviews

def save_to_csv(reviews: list, filename: str = 'scraped_reviews.csv'):
    """
    Menyimpan data ulasan aplikasi ke dalam file CSV.
    
    Args:
        reviews (list): Daftar ulasan yang akan disimpan.
        filename (str): Nama file CSV (default 'scraped_reviews.csv').
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['review_id', 'user_name', 'score', 'date', 'text'])
        writer.writeheader()
        for review in reviews:
            writer.writerow({
                'review_id': review['reviewId'],
                'user_name': review['userName'],
                'score': review['score'],
                'date': review['at'],
                'text': review['content']
            })

app_id = 'id.bmri.livin'
reviews = scrape_reviews(app_id, count=12000)
save_to_csv(reviews)

print(f"Data ulasan untuk aplikasi {app_id} telah disimpan ke dalam file 'scraped_reviews.csv'.")
