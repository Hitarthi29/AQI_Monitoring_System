from model import AQIDatabase
from controller import AQIDataFetcher

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '******',
    'database': 'AQI'
}

def main():
    print("Fetching AQI data...")
    raw_data = AQIDataFetcher.fetch_data()
    processed_data = AQIDataFetcher.process_data(raw_data)
    print(f"Fetched and processed {len(processed_data)} city records.")

    db = AQIDatabase(**DB_CONFIG)
    db.insert_aqi_data(processed_data)
    db.close()
    print(f"Inserted {len(processed_data)} records into the database.")

if __name__ == "__main__":
    main()
