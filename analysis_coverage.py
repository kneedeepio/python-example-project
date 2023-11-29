#!/usr/bin/env python3

### IMPORTS ###
import coverage
import logging
import os
import sys

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###

### MAIN ###
def main():
    logging.basicConfig(level = logging.DEBUG)

    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    SOURCE_PATHS = [
        os.path.join(BASE_PATH, 'example'),
        # Add libraries here
        os.path.join(BASE_PATH, 'tests')
    ]
    REPORT_PATH = os.path.join(BASE_PATH, 'coverage_report')
    if not os.path.isdir(REPORT_PATH):
        os.mkdir(REPORT_PATH)

    COV = coverage.Coverage(source = SOURCE_PATHS)
    COV.start()

    # Ugly import is needed to get accurate test coverage reporting
    from tests import run_all_tests  # pylint: disable=wrong-import-position

    SUCCESS = run_all_tests()

    COV.stop()

    COV.html_report(directory = REPORT_PATH)

    logging.shutdown()

    if SUCCESS is False:
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    main()

