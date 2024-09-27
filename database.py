import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Get the absolute path to the database file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_PATH = os.path.join(BASE_DIR, 'jujitsu_popularity.db')

# Create the full database URI
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Create the engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print(f"Database path: {DATABASE_PATH}")
