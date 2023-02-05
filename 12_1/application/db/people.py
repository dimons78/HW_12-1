from datetime import date


def get_employees():
    print("This get_employees")
    now_ = date.today()
    print(now_)
    print("day:", now_.day, "month:",  now_.month, "year:", now_.year)
