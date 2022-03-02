from enum import Enum

from console import Console


class InputWrongPatientId(Exception):

    def __init__(self):
        super().__init__("Ошибка ввода. ID пациента должно быть числом (целым, положительным)")


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

    def __init__(self, console=None):
        self._console = console if console is not None else Console()

    def print_current_patient_status(self, status):
        self._console.print(f'Статус пациента: "{status}"')

    def print_new_patient_status(self, status):
        self._console.print(f'Новый статус пациента: "{status}"')

    def print_stop_session(self):
        self._console.print("Сеанс завершён.")

    def print_statistics(self, statistics):
        self._console.print("Статистика по статусам:")
        for statistics_part in statistics:
            self._console.print(f' - в статусе "{statistics_part.status}": {statistics_part.patients_number} чел.')

    def get_patient_id(self) -> int:
        patient_id = self._console.input("Введите ID пациента:")
        try:
            return int(patient_id)
        except ValueError:
            raise InputWrongPatientId

    def get_command(self) -> CommandTypes:
        command = self._console.input("Введите команду:")
        parsed_command = None
        try:
            parsed_command = CommandTypes(command)
        except ValueError:
            self._console.print("Неизвестная команда! Попробуйте ещё раз.")
        return parsed_command
