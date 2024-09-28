from database import SessionLocal
from models import PopularityData
import matplotlib.pyplot as plt
import warnings
from sklearn.linear_model import LinearRegression
import pandas as pd
warnings.filterwarnings("ignore")


def generate_static_popularity_chart():
    # Create a database session
    db = SessionLocal()
    try:
        # Query the database for popularity data ordered by date
        data = db.query(PopularityData).order_by(PopularityData.date).all()
        dates = [entry.date for entry in data]
        scores = [entry.popularity_score for entry in data]

        # Convert dates to ordinal for regression analysis
        dates_ordinal = [d.toordinal() for d in dates]

        # Create a DataFrame for easier manipulation
        df = pd.DataFrame({'Date': dates, 'Score': scores, 'Date_Ordinal': dates_ordinal})

        # Linear regression for trend line
        model = LinearRegression()
        model.fit(df[['Date_Ordinal']], df['Score'])

        # Predict scores using the linear model to create a trend line
        trend_scores = model.predict(df[['Date_Ordinal']])

        # Create a Matplotlib figure
        plt.figure(figsize=(10, 6))
        plt.plot(df['Date'], df['Score'], label='Popularity Score', color='blue', linestyle='-', marker=None)

        # Plot the trend line
        plt.plot(df['Date'], trend_scores, label='Trend Line', color='red', linestyle='--')

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