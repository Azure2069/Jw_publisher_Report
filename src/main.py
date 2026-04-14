from fastapi import FastAPI
from web.elder import router as elder_router
from model.elder import Base
from database.database_init import engine




app=FastAPI()

app.include_router(elder_router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
