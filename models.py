from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import Column, Integer, String
import dotenv
import os

dotenv.load_dotenv()

name = os.getenv("PG_USER")
password = os.getenv("PG_PASSWORD")
database = os.getenv("PG_DB")

PG_DSN = f"postgresql+asyncpg://{name}:{password}@127.0.0.1:5432/{database}"
engine = create_async_engine(PG_DSN)
Base = declarative_base()
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class SwapiPeople(Base):
    __tablename__ = "swapi_people"

    id = Column(Integer, primary_key=True)
    birth_year = Column(String)
    eye_color = Column(String)
    films = Column(String)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(String)
    homeworld = Column(String)
    mass = Column(String)
    name = Column(String)
    skin_color = Column(String)
    species = Column(String)
    starships = Column(String)
    vehicles = Column(String)


