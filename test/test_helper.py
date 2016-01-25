import unittest

def get_file_name(args):
    if args['-f']:
        return args['-f'] + '.py'
    return '*test.py'


def get_class_name(args):
    if args['-c']:
        return args['-c']
    return ''


def run_test_class(suites, class_name):
    suite_list = unittest.TestSuite()
    for suite in suites:
        for test_case in suite:
            for test in test_case:
                if class_name == test.__class__.__name__:
                    suite_list.addTest(test)
    return unittest.TextTestRunner(verbosity=0, failfast=True).run(suite_list)


def run_suite_test(args):
    t = unittest.TestLoader()
    name = get_file_name(args)
    suites = t.discover('test', pattern=name)
    class_name = get_class_name(args)
    if class_name != '':
        return run_test_class(suites, class_name)
    return unittest.TextTestRunner(verbosity=0, failfast=True).run(suites)

def run_unit_test(args):
    t = args.copy()
    return run_suite_test(t)


def check_error(result):
    if len(result.failures) > 0 or len(result.errors):
        return 1
    return 0


def get_args(args, values):

    for i in range(0, len(args)):
        if args[i] == '-f' or args[i] == '-c':
            values[args[i]] = args[i + 1]
        if args[i] == 'it':
            values['it'] = True
