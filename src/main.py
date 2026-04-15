from fastapi import FastAPI
from web.elder import router as elder_router
from database.database_init import engine, Base
from model.elder import Elder
from model.users import Groups, All_Users




app=FastAPI()

app.include_router(elder_router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
