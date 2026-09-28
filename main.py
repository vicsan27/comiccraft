from fastapi import FastAPI
import routes

app = FastAPI(title="ComicCraft")
app.include_router(routes.router)