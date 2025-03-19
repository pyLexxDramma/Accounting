import datetime

from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    print("Текущая дата:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    calculate_salary()
    get_employees()
