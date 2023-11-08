import unittest
import sys
import argparse
import yaml

from tests_ems_mticket_flow import EmsFlow
from tests_ems_mticket_testcase import EmsMticketTestCase

def tests_suite():
    suite = unittest.TestSuite()
    suite.addTest(EmsFlow())
    return suite


def configure(config, environment):
    environments = config.get('environments')
    selected_environment = environments.get(environment)
    EmsMticketTestCase._URL = selected_environment.get('url')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('env', choices=['prod', 'test'])
    args = parser.parse_args()
    config = yaml.load(open('config.yml'), Loader=yaml.FullLoader)
    configure(config, args.env)
    runner = unittest.TextTestRunner(resultclass=unittest.TextTestResult)
    result = unittest.TextTestRunner(verbosity=1, ).run(tests_suite())
    sys.exit(not result.wasSuccessful())
