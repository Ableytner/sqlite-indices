import sqlalchemy
import sqlalchemy.ext.declarative

Base = sqlalchemy.ext.declarative.declarative_base()

class Person(Base):
    """Person representation."""

    __tablename__ = "person"
    person_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String)
    sure_name = sqlalchemy.Column(sqlalchemy.String)

class PersonIdx(Base):
    """Person with indeces representation."""

    __tablename__ = "person_idx"
    person_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String, index=True)
    sure_name = sqlalchemy.Column(sqlalchemy.String, index=True)
