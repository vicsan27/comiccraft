from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

def generate_dummy_comic(theme: str, panels: int = 4):
    base = [
        {"title": "Panel 1 - Aarambam", "description": f"{theme} - kadhai aarambam.", "dialogue": "Wow! Pudhu naal!"},
        {"title": "Panel 2 - Problem", "description": "Oru problem varudhu.", "dialogue": "Aiyo! Enna idhu?"},
        {"title": "Panel 3 - Plan", "description": "Hero plan poduran.", "dialogue": "Enakku idea iruku!"},
        {"title": "Panel 4 - Climax", "description": "Problem solve.", "dialogue": "Namma jeyichitom!"},
    ]
    return base[:panels]

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"comics": None})

@router.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, theme: str = Form(...), panel_count: int = Form(4)):
    comics = generate_dummy_comic(theme, panel_count)
    return templates.TemplateResponse(request=request, name="index.html", context={"comics": comics, "theme": theme})