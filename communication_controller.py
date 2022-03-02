from enum import Enum


class CommandTypes(Enum):
    def __new__(cls, value_en: str, value_ru: str):
        obj = object.__new__(cls)
        obj._value_ = value_en
        obj._value_ru = value_ru
        cls._value2member_map_[value_en] = obj
        cls._value2member_map_[value_ru] = obj

        return obj

    PATIENT_STATUS = ("узнать статус пациента", "get id")
    STATUS_UP = ("повысить статус пациента", "status up")
    STATUS_DOWN = ("понизить статус пациента", "status down")
    CALCULATE_STATISTICS = ("рассчитать статистику", "calculate statistics")
    STOP = ("стоп", "stop")



class CommunicationController:

    def __init__(self):
        pass