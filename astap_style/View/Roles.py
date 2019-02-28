from enum import Enum


class Roles(Enum):
    CropRotation = 0
    Deals = 1
    Techniques = 2
    Rig = 3
    Dictionaries = 4

    Owner = "Хозяин фермы"

    Technical_engineer = "Технический инженер"
    Technological_engineer = "Инженер технолог"
    Lawyer = "Юрист"
    Tractor_Driver = "Комбайнер"
    Undifiend = "Роль не определена"
