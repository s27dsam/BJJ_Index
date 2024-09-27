from models import Base
from database import engine

Base.metadata.drop_all(bind=engine)  # This will drop all tables
Base.metadata.create_all(bind=engine)  # This will create them again


print("Tables created successfully!")