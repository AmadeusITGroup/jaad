#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ["PYTHONHASHSEED"] = "0"
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa F401
        except ImportError:
            raise ImportError(
                "Could not import Django. Are you sure it is installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
