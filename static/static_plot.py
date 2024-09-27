from database import SessionLocal
from models import PopularityData
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


def generate_static_popularity_chart():
    # Create a database session
    db = SessionLocal()
    try:
        # Query the database for popularity data ordered by date
        data = db.query(PopularityData).order_by(PopularityData.date).all()
        dates = [entry.date for entry in data]
        scores = [entry.popularity_score for entry in data]

        # Create a Matplotlib figure
        plt.figure(figsize=(10, 6))
        plt.plot(dates, scores, label='Popularity Score', color='blue', linestyle='-', marker=None)

        # Add title and labels
        plt.title('Jujitsu Popularity Over Time')
        plt.xlabel('Date')
        plt.ylabel('Popularity Score')

        # Add grid and legend
        plt.grid(True)
        plt.legend()

        # Save the plot to a file or display it
        plt.savefig('pop_chart_static.png')  # Saves the plot as a PNG file
        plt.show()  # Displays the plot in a window
    finally:
        db.close()



generate_static_popularity_chart()