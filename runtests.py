#!/usr/bin/env python
import sys
import django

from django.conf import settings
from django.test.utils import get_runner


def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True, failfast=False)
    failures = test_runner.run_tests(['tidyenum', ])
    sys.exit(failures)


if __name__ == '__main__':
    django.setup()
    runtests()
