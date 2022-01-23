import warnings

from sqlalchemy import exc as sa_exc

from test_speed import TestSpeed

def main():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=sa_exc.SAWarning)

        TestSpeed.create_db(3)
        TestSpeed.start_tests("kga")

if __name__ == "__main__":
    main()
