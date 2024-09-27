from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from chart import generate_popularity_chart

app = FastAPI()

# Mount the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def popularity_chart(request: Request):
    graph_html = generate_popularity_chart()
    return templates.TemplateResponse("index.html", {"request": request, "graph_html": graph_html})


@app.get('/summary')
async def get_summary():
    with open('summary.txt', 'r') as f:
        summary = f.read()
    return {'summary': summary}
