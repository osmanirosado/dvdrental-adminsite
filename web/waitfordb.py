import os
import sys
import time

from django.db import connection
from django.db.utils import OperationalError


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

    n = 1  # attempt number
    h = 60  # last attempt
    b = 2  # growth factor
    s = 1  # time in seconds to wait if the connection to the database fails in attempt n
    sys.stdout.write('Waiting for database...\n')
    while n <= h:
        try:
            connection.ensure_connection()
            sys.stdout.write('Database available!\n\n')
            sys.stdout.flush()
            file = sys.argv[1]
            args = sys.argv[1:]  # first argument is the program name
            os.execvp(file, args)  # execute the command, replacing the current process
        except OperationalError:
            sys.stdout.write(f' [{n}/{h}] Database unavailable, waiting for {s} seconds ...\n')
            sys.stdout.flush()
            time.sleep(s)
            n = n + 1  # increase attempt number
            s = s * b  # calculate wait time for next attempt
    sys.exit(1)


if __name__ == '__main__':
    main()
