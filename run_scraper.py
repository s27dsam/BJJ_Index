from backend.scraper import get_all_and_get_overall_average, store_popularity_data

if __name__ == "__main__":
    print("Starting to collect BJJ popularity data...")
    popularity_data = get_all_and_get_overall_average()
    print("Data collected. Storing in database...")
    store_popularity_data(popularity_data)
    print("Done! Data has been stored in the database.")
