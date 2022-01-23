from os.path import isfile
from os import remove
import time

from db_creator import DBCreator
from db_manager import DBManager

class TestSpeed():
    def __init__(self) -> None:
        pass

    def create_db(self, digits):
        if isfile("./test.db"):
            remove("./test.db")

        db_creator = DBCreator(digits, False)
        db_creator.create_persons()

        db_creator_idx = DBCreator(digits, True)
        db_creator_idx.create_persons()

    def start_tests(self):
        without_idx = []
        with_idx = []

        manager = DBManager(False)
        without_idx.append(time.perf_counter())
        manager.select_person("rbx", "Smith")
        without_idx.append(time.perf_counter())

        manager_idx = DBManager(True)
        with_idx.append(time.perf_counter())
        manager_idx.select_person("rbx", "Smith")
        with_idx.append(time.perf_counter())

        print(f"Without indices: {without_idx[1] - without_idx[0]:0.4f}")
        print(f"With indices:    {with_idx[1] - with_idx[0]:0.4f}")
