from fastapi import FastAPI
from app.views.routes import router

app = FastAPI(title="Calculadora MVC")
app.include_router(router)