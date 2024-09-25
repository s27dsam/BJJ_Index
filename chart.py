from database import SessionLocal
from models import PopularityData
import plotly.graph_objs as go
from plotly.offline import plot


def generate_popularity_chart():
    db = SessionLocal()
    try:
        data = db.query(PopularityData).order_by(PopularityData.date).all()
        dates = [entry.date for entry in data]
        scores = [entry.popularity_score for entry in data]

        # Create a Plotly figure
        fig = go.Figure(data=[
            go.Scatter(x=dates, y=scores, mode='lines', name='Popularity Score')
        ])

        fig.update_layout(
            title='Jujitsu Popularity Over Time',
            xaxis_title='Date',
            yaxis_title='Popularity Score'
        )

        # Convert the figure to HTML div string
        graph_html = plot(fig, output_type='div', include_plotlyjs=False)
        return graph_html
    finally:
        db.close()

