from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

# ENGINE = None
# Session = None

ENGINE = create_engine("sqlite:///ratings.db", echo=True)
session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)

    def __repr__(self):
        return "<User email=%s password=%s age=%d zipcode=%s>" % (self.email, self.password, self.age, self.zipcode)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    release_date = Column(DateTime, nullable=True)
    url = Column(String(128), nullable=True)


    def __repr__(self):
        return "<Movie id=%s title=%s release date=%s url=%s>" % (self.id, self.title, self.release_date, self.url)

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    rating = Column(Integer, nullable=False)

    user = relationship("User",
            backref=backref("ratings", order_by=id))

    movie = relationship("Movie",
            backref=backref("ratings", order_by=id))


    def __repr__(self):
        return "<user id=%s movie id=%s rating=%s>" % (self.user_id, self.movie_id, self.rating)


### End class declarations
def connect():
    # global ENGINE
    # global Session
    pass
    # return Session()


def main():
    """In case we need this for something"""

if __name__ == "__main__":
    main()
