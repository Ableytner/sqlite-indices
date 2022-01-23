import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker

from model import Base, Person, PersonIdx

class DBManager():
    def __init__(self, use_indeces):
        self.use_indeces = use_indeces

        db_connection = sqlalchemy.create_engine("sqlite:///test.db", connect_args={'check_same_thread': False})
        Base.metadata.create_all(db_connection)

        session_factory = sessionmaker(db_connection)
        self._Session = scoped_session(session_factory)
        self.session = self._Session()

    def __delete__(self):
        self._Session.remove()

    def create_person(self, first_name, sure_name):
        if self.use_indeces:
            new_person = PersonIdx(first_name=first_name, sure_name=sure_name)
        else:
            new_person = Person(first_name=first_name, sure_name=sure_name)

        self.session.add(new_person)

    def commit(self):
        self.session.commit()

    def select_person(self, first_name, sure_name):
        if self.use_indeces:
            stmt = sqlalchemy.select(PersonIdx).where(PersonIdx.first_name == first_name and PersonIdx.sure_name == sure_name)
        else:
            stmt = sqlalchemy.select(Person).where(Person.first_name == first_name and Person.sure_name == sure_name)

        result = self.session.execute(stmt)

        for person_obj in result.scalars():
            print(f"{person_obj.first_name} / {person_obj.sure_name}")

    def get_person_by_index(self, index):
        if self.use_indeces:
            return self.session.query(PersonIdx).get(index)
        else:
            return self.session.query(Person).get(index)
