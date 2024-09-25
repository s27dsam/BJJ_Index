from models import PopularityData
from database import SessionLocal


# Function to store the popularity data into the database
def store_popularity_data(data):
    db = SessionLocal()
    try:
        # Loop through each row in the DataFrame
        for index, row in data.iterrows():
            db_data = PopularityData(
                date=row['date'],  # Store the date
                metric1=row['bjj'],
                metric2=row['brazilian_jiu_jitsu'],
                metric3=row['jujitsu'],
                popularity_score=row['average']
            )
            db.add(db_data)
        db.commit()  # Commit the transaction to the database
    finally:
        db.close()  # Close the connection
