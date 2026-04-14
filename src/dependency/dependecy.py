from database.database_init import SessionLocal

def db_add():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()