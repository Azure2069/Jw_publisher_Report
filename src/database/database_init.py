from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url="postgresql+psycopg2://postgres:postgres@localhost:5432/anyaa_north"
engine=create_engine(db_url)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)




