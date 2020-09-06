def validate_name(name):
    checkname = ["1", "2", "3", "4", "5", "6", "7",
                 "8", "9", "0", "!", "@", "#", "$", " "]
    name = str(name)
    if len(name) == 0:
        return False
    for i in name:
        if i in checkname:
            return False
    return True


def validate_id(id):
    return True


def validate_phone_number(phone_number):
    return True
