import pytest

from unittest.mock import MagicMock

from application import Application
from communication_controller import CommunicationController
from hospital import Hospital
from hospital_controller import HospitalController
from patient import Patient
from tests.mocks.console_mock import ConsoleMock


def test_change_patients_status():
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)
    hospital = Hospital(
        [Patient(1, 1), Patient(2, 1)]
    )
    expected_hospital = Hospital(
        [Patient(1, 0), Patient(2, 2)]
    )
    hospital_controller = HospitalController(hospital, communication_controller)
    application = Application(communication_controller, hospital_controller)

    console_mock.add_expected_input("Введите команду:", "повысить статус пациента")
    console_mock.add_expected_input("Введите ID пациента:", "2")
    console_mock.add_expected_print('Новый статус пациента: "Слегка болен"')

    console_mock.add_expected_input("Введите команду:", "понизить статус пациента")
    console_mock.add_expected_input("Введите ID пациента:", "1")
    console_mock.add_expected_print('Новый статус пациента: "Тяжело болен"')

    console_mock.add_expected_input("Введите команду:", "стоп")
    console_mock.add_expected_print("Сеанс завершён.")

    application.exec()
    console_mock.check_all_mocks_used()
    assert hospital == expected_hospital, "После выполнения команд состояние больницы не соответствует ожидаемому"


def test_patients_status_manipulations():
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)
    hospital = Hospital(
        [Patient(1, 1), Patient(2, 1), Patient(3, 1)]
    )
    expected_hospital = Hospital(
        [Patient(1, 1), Patient(2, 2), Patient(3, 0)]
    )
    hospital_controller = HospitalController(hospital, communication_controller)
    application = Application(communication_controller, hospital_controller)

    console_mock.add_expected_input(expected_text="Введите команду:", expected_input="узнать статус пациента")
    console_mock.add_expected_input("Введите ID пациента:", "1")
    console_mock.add_expected_print(print_text="Болен")

    console_mock.add_expected_input("Введите команду:", "повысить статус пациента")
    console_mock.add_expected_input("Введите ID пациента:", "2")
    console_mock.add_expected_print('Новый статус пациента: "Слегка болен"')

    console_mock.add_expected_input("Введите команду:", "понизить статус пациента")
    console_mock.add_expected_input("Введите ID пациента:", "3")
    console_mock.add_expected_print('Новый статус пациента: "Тяжело болен"')

    console_mock.add_expected_input("Введите команду:", "рассчитать статистику")
    console_mock.add_expected_print("Статистика по статусам:")
    console_mock.add_expected_print('- в статусе "Тяжело болен": 1 чел.')
    console_mock.add_expected_print('- в статусе "Болен": 1 чел.')
    console_mock.add_expected_print('- в статусе "Слегка болен": 1 чел.')

    console_mock.add_expected_input("Введите команду:", "стоп")
    console_mock.add_expected_print("Сеанс завершён.")

    application.exec()
    console_mock.check_all_mocks_used()

    assert hospital == expected_hospital, "После выполнения команд состояние больницы не соответствует ожидаемому"


def test_non_existent_command():
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)
    hospital_controller = MagicMock()
    application = Application(communication_controller, hospital_controller)

    console_mock.add_expected_input(expected_text="Введите команду:", expected_input="выписать всех пациентов")
    console_mock.add_expected_print(print_text="Неизвестная команда! Попробуйте ещё раз.")

    console_mock.add_expected_input("Введите команду:", "стоп")
    console_mock.add_expected_print("Сеанс завершён.")

    application.exec()
    console_mock.check_all_mocks_used()


@pytest.mark.parametrize(
    "wrong_id", ("два", "1,2", "1.2")
)
def test_wrong_patient_id(wrong_id):
    console_mock = ConsoleMock()
    communication_controller = CommunicationController(console_mock)
    hospital = MagicMock()
    hospital_controller = HospitalController(hospital, communication_controller)
    application = Application(communication_controller, hospital_controller)

    console_mock.add_expected_input(expected_text="Введите команду:", expected_input="status up")
    console_mock.add_expected_input("Введите ID пациента", wrong_id)
    console_mock.add_expected_print(print_text="Ошибка ввода. ID пациента должно быть числом (целым, положительным)")

    console_mock.add_expected_input("Введите команду:", "стоп")
    console_mock.add_expected_print("Сеанс завершён.")

    application.exec()
    console_mock.check_all_mocks_used()
