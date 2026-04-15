from fastapi import FastAPI
from web.elder import router as elder_router
from database.database_init import engine, Base
from model.elder import Elder
from model.users import Groups, All_Users
from web.publisher_web import router as publisher_router




app=FastAPI()

app.include_router(elder_router)
app.include_router(publisher_router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
