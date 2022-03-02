import pytest

from communication_controller import CommunicationController, CommandTypes, InputWrongPatientId
from dto import StatisticsPartDto
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


def test_print_end_session():
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)
    console_mock.add_expected_print("Сеанс завершён.")

    communication_controller.print_stop_session()
    console_mock.check_all_mocks_used()


def test_get_patient_id():
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)
    console_mock.add_expected_input("Введите ID пациента:", "1")

    patient_id = communication_controller.get_patient_id()
    assert patient_id == 1, "Получен неверный id "
    console_mock.check_all_mocks_used()


@pytest.mark.parametrize(
    "wrong_id", ("1.2", "1,2", "два")
)
def test_get_wrong_patient_id(wrong_id):
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)
    console_mock.add_expected_input("Введите ID пациента:", "wrong_id")

    with pytest.raises(InputWrongPatientId):
        communication_controller.get_patient_id()
    console_mock.check_all_mocks_used()


def test_print_statistics():
    statistics = [
        StatisticsPartDto(status="Тяжело болен", patients_number=1),
        StatisticsPartDto(status="Болен", patients_number=198),
        StatisticsPartDto(status="Слегка болен", patients_number=1)
    ]
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)
    console_mock.add_expected_print("Статистика по статусам:")
    console_mock.add_expected_print(' - в статусе "Тяжело болен": 1 чел.')
    console_mock.add_expected_print(' - в статусе "Болен": 198 чел.')
    console_mock.add_expected_print(' - в статусе "Слегка болен": 1 чел.')

    communication_controller.print_statistics(statistics)
    console_mock.check_all_mocks_used()
