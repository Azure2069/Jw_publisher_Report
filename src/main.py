from fastapi import FastAPI
#from web.elder import router as elder_router
from database.database_init import engine, Base
from web.report import router as report_router


#from web.publisher_web import router as publisher_router
from web.user import router as user_router




app=FastAPI()

#app.include_router(elder_router)
#app.include_router(publisher_router)
app.include_router(user_router)
app.include_router(report_router)
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
