import datetime

from application.db.people import *
from application.salary import *

if __name__ == '__main__':
    now = datetime.datetime.now()
    print(f"Текущая дата (dirty_main): {now.strftime('%Y-%m-%d %H:%M:%S')}")

    calculate_salary()
    get_employees()
