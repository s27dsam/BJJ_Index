from database import SessionLocal
from models import PopularityData



def generate_popularity_chart():
    db = SessionLocal()
    try:
        # Retrieve data from the database, ordered by date
        data = db.query(PopularityData).order_by(PopularityData.date).all()
        dates = [entry.date.strftime("%Y-%m-%d") for entry in data]  # Format dates as strings
        scores = [entry.popularity_score for entry in data]
        return dates, scores
    finally:
        db.close()
