import pytest

from communication_controller import CommunicationController, CommandTypes
from tests.mocks.console_mock import ConsoleMock


def test_command_types_work():
    assert CommandTypes("узнать статус пациента") == CommandTypes.PATIENT_STATUS
    assert CommandTypes("get id") == CommandTypes.PATIENT_STATUS


@pytest.mark.parametrize(
    "command,expected_command_type",
    (
        ("узнать статус пациента", CommandTypes.PATIENT_STATUS),
        ("get id", CommandTypes.PATIENT_STATUS),

        ("повысить статус пациента", CommandTypes.PATIENT_STATUS),
        ("status up", CommandTypes.PATIENT_STATUS),

        ("понизить статус пациента", CommandTypes.PATIENT_STATUS),
        ("status down", CommandTypes.PATIENT_STATUS),

        ("рассчитать статистику", CommandTypes.PATIENT_STATUS),
        ("calculate statistics", CommandTypes.PATIENT_STATUS),

        ("стоп", CommandTypes.PATIENT_STATUS),
        ("stop", CommandTypes.PATIENT_STATUS),
    )
)
def test_get_command_from_text(command, expected_command_type):
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)
    console_mock.add_expected_input("Введите команду:", command)

    parsed_command = communication_controller.get_command()
    assert parsed_command == expected_command_type, "Команда спарсилась в неверный результат"


def test_print_patient_current_status():
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)



def test_print_patient_new_status():
    pass
