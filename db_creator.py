from datetime import datetime
from itertools import product
from threading import Thread
from time import sleep

from db_manager import DBManager

class DBCreator():
    def __init__(self, digits, use_indeces) -> None:
        self.digits = digits
        self.start_time = None

        self.written_persons = 0
        self.total_persons = 0

        self.db_manager = DBManager(use_indeces)

    def create_persons(self):
        self.start_time = datetime.now()

        characters = []
        for i in range(26):
            characters.append(chr(i + 97))

        self.total_persons = len(characters)**self.digits

        gui_thread = Thread(target=self._gui_func)
        gui_thread.start()

        self._generate_persons(characters)

    def _generate_persons(self, characters):
        persons = []
        person_counter = 0

        for x in self._create_persons_yield(characters):
            persons.append(''.join(x))
            person_counter += 1

            if person_counter >= 10000:
                self._write_and_commit_persons(persons)
                persons.clear()
                person_counter = 0

        self._write_and_commit_persons(persons)

    def _create_persons_yield(self, characters):
        yield from product(*([characters] * self.digits))

    def _write_and_commit_persons(self, persons):
        for person in persons:
            self.db_manager.create_person(person, "Smith")
            self.written_persons += 1

        self.db_manager.commit()

    def _gui_func(self):
        while self.written_persons < self.total_persons:
            print("Written to db: " + str(self.written_persons) + "/" + str(self.total_persons) + ", Elapsed: " + str(datetime.now() - self.start_time).split(".")[0], end="\r")
            sleep(0.25)

        print("Written to db: " + str(self.written_persons) + "/" + str(self.total_persons) + ", Elapsed: " + str(datetime.now() - self.start_time).split(".")[0])
