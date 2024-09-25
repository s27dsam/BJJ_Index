from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from chart import generate_popularity_chart

app = FastAPI()

# scheduler = BackgroundScheduler()
# scheduler.add_job(daily_update, 'cron', hour=0)  # Runs daily at midnight
# scheduler.start()

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")


@app.get("/popularity", response_class=HTMLResponse)
async def popularity_chart(request: Request):
    graph_html = generate_popularity_chart()
    return templates.TemplateResponse("popularity.html", {"request": request, "graph_html": graph_html})


@app.get('/summary')
async def get_summary():
    with open('summary.txt', 'r') as f:
        summary = f.read()
    return {'summary': summary}
