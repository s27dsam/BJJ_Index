from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from chart import generate_popularity_chart
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Mount the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Environment variables for RapidAPI (if applicable)
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "google-news13.p.rapidapi.com"

# Endpoint to fetch news data (commented out as per your current requirement)
# def fetch_news():
#     # Your existing fetch_news implementation
#     pass


@app.get("/index", response_class=HTMLResponse)
async def popularity_chart(request: Request):
    # Generate your existing graph data
    dates, scores = generate_popularity_chart()

    # Fetch the latest news (commented out as per your current requirement)
    # try:
    #     latest_news = fetch_news()
    # except HTTPException as e:
    #     latest_news = []
    #     error_message = "Unable to fetch latest news at the moment."

    # Pass both graph and news data to the template
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "dates": dates,       # Pass dates to the template
            "scores": scores,     # Pass scores to the template
            # "latest_news": latest_news,   # Pass the news data here if needed in the future
            # "error_message": error_message if 'error_message' in locals() else None
        }
    )


@app.get('/summary')
async def get_summary():
    with open('summary.txt', 'r') as f:
        summary = f.read()
    return {'summary': summary}


