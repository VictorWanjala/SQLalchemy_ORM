import random
from faker import Faker
from main import Student
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()  #similar to cursor in sqlite3

fake = Faker()
students = [
    Student(
        name = fake.name(),
        index = random.randint(900,1900)
    )
    for s in range(20)]
session.bulk_save_objects(students)
session.commit()
