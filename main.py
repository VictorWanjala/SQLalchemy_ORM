##Installation guide
# 1.create project folder
# 2.Create files - python file(i.e, main.py), Pipfile, db.py
# 3.pipenv install
# 4.pipenv shell
# 5.pipenv install sqlalchemy
# 6.add shebang line in your python file to make the file executable//!usr/bin/python3
# 7.run chmod a+x [python file name- i.e, main.py] to give execution permission




#!usr/bin/python3
from sqlalchemy import Column, Index, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__= 'students'
    #table columns
    id = Column(Integer(),primary_key=True)
    name = Column(String())
    index = Column(Integer())



    #connecting to database
if __name__=='__main__':#//Checking if this is the main file as processed
                        # in the terminal using chmod a+x main.py
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()  #similar to cursor in sqlite3

    #reading data
    studs = session.query(Student).all()
    display_studs = [studs.name for studs in studs if studs.id == 1]
    print(display_studs)
    #del data
    studentdel = session.query(Student).filter(Student.id == 1).first()
    studentdel = session.query(Student).filter(Student.name.like("%Vic%")).first()

    session.delete(studentdel)
    session.commit()
    print(studentdel)
    #create data function with sqlalchemy
    studentA = Student(
        name = 'Max',
        index = 123
    )
    studentB = Student(
        name = 'Vic',
        index = 124
    )
    # print(studentA.name, studentB.name)
    session.bulk_save_objects([studentA,studentB])
    session.commit()
    #update data
    session.query(Student).update({Student.name : 'Max'})
    session.commit()


    


