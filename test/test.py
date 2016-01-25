import sys
import os
from test_helper import run_suite_test, check_error, get_args, run_unit_test

sys.path.append(os.path.abspath('./'))

values = dict()
values['-f'] = None
values['-c'] = None

def execute():
    get_args(sys.argv, values)
    if values['-c'] or values['-f']:
        return run_unit_test(values)
    if check_error(run_unit_test(values)) > 0:
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(execute())
