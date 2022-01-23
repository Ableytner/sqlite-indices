import warnings

from sqlalchemy import exc as sa_exc

from db_creator import DBCreator
from test_speed import TestSpeed

def main():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=sa_exc.SAWarning)

        # db_creator = DBCreator(3, False)
        # db_creator.create_persons()

        tester = TestSpeed()
        tester.create_db(3)
        # tester.start_tests()

if __name__ == "__main__":
    main()
