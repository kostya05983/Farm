import re


def validate_email(value):
    if not re.fullmatch(
            "^[-a-z0-9!#$%&'*+/=?^_`{|}~]+(?:\.[-a-z0-9!#$%&'*+/=?^_`{|}~]+)" \
            + "*@(?:[a-z0-9]([-a-z0-9]{0,61}[a-z0-9])?\.)" \
            + "*(?:aero|arpa|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi" \
            + "|museum|name|net|org|pro|tel|travel|[a-z][a-z])$", value):
        return False
    return True


def validate_date(value):
    if not re.fullmatch("([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", value):
        return False
    return True


def validate_phone_number(value):
    if not re.fullmatch("^((\+7|7|8)+([0-9]){10})$", value):
        return False
    return True


def validate_time(time):
    if not time:
        return -1
    result = re.fullmatch('\d*', time)
    if result is None:
        return -1
    if int(time) <= 0:
        return -1
    return 1


def validate_number(year):
    if not year:
        return -1
    result = re.fullmatch('\d*', year)

    if result is None:
        return -1
    return 1


def validate_requisites(value):
    if not re.fullmatch("\d*", value):
        return False
    return True
