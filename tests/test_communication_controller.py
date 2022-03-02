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

        ("повысить статус пациента", CommandTypes.STATUS_UP),
        ("status up", CommandTypes.STATUS_UP),

        ("понизить статус пациента", CommandTypes.STATUS_DOWN),
        ("status down", CommandTypes.STATUS_DOWN),

        ("рассчитать статистику", CommandTypes.CALCULATE_STATISTICS),
        ("calculate statistics", CommandTypes.CALCULATE_STATISTICS),

        ("стоп", CommandTypes.STOP),
        ("stop", CommandTypes.STOP),
    )
)
def test_get_command_from_text(command, expected_command_type):
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)
    console_mock.add_expected_input("Введите команду:", command)

    parsed_command = communication_controller.get_command()
    assert parsed_command == expected_command_type, "Команда спарсилась в неверный результат"
    console_mock.check_all_mocks_used()


def test_get_wrong_command_from_text():
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)
    console_mock.add_expected_input("Введите команду:", "Выписать всех")
    console_mock.add_expected_print("Неизвестная команда! Попробуйте ещё раз.")

    parsed_command = communication_controller.get_command()
    assert parsed_command is None, "Команда спарсилась в неверный результат"
    console_mock.check_all_mocks_used()


def test_print_patient_current_status():
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)
    console_mock.add_expected_print('Статус пациента: "Болен"')

    communication_controller.print_current_patient_status("Болен")
    console_mock.check_all_mocks_used()


def test_print_patient_new_status():
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)
    console_mock.add_expected_print('Новый статус пациента: "Готов к выписке"')

    communication_controller.print_new_patient_status("Готов к выписке")
    console_mock.check_all_mocks_used()
