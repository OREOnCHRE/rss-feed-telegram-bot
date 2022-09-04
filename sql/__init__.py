import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = os.environ.get("postgres://fwcetpcafvdpkp:05e903e12d8dcd2913d841775aeb09ee03915f98b09175ae92e313be20100d3f@ec2-44-193-178-122.compute-1.amazonaws.com:5432/d3j9q4ep29a405")

def start() -> scoped_session:
    engine = create_engine(os.environ.get("postgres://fwcetpcafvdpkp:05e903e12d8dcd2913d841775aeb09ee03915f98b09175ae92e313be20100d3f@ec2-44-193-178-122.compute-1.amazonaws.com:5432/d3j9q4ep29a405"))
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    # this is a dirty way for the work-around required for #23
    print("DATABASE_URL is not configured. Features depending on the database might have issues.")
    print(str(e))
