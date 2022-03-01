import pytest

from tests.mocks.console_mock import ConsoleMock


def test_patients_status_manipulations():
    console_mock = ConsoleMock()
    hospital = Hospital(
        [Patient(1, 1), Patient(2, 1), Patient(3, 1)]
    )
    expected_hospital = Hospital(
        [Patient(1, 1), Patient(2, 2), Patient(3, 0)]
    )
    application = Application(console_mock, hospital)
    console_mock.add_expected_input(expected_text="Введите команду", expected_input="узнать статус пациента")
    console_mock.add_expected_input("Введите ID пациента", "1")
    console_mock.add_expected_print(print_text="Болен")

    console_mock.add_expected_input("Введите команду", "повысить статус пациента")
    console_mock.add_expected_input("Введите ID пациента", "2")
    console_mock.add_expected_print("Слегка болен")

    console_mock.add_expected_input("Введите команду", "понизить статус пациента")
    console_mock.add_expected_input("Введите ID пациента", "3")
    console_mock.add_expected_print("Тяжело болен")

    console_mock.add_expected_input("Введите команду", "рассчитать статистику")
    console_mock.add_expected_print("Статистика по статусам:")
    console_mock.add_expected_print('- в статусе "Тяжело болен": 1 чел.')
    console_mock.add_expected_print('- в статусе "Болен": 1 чел.')
    console_mock.add_expected_print('- в статусе "Слегка болен": 1 чел.')

    console_mock.add_expected_input("Введите команду", "стоп")
    console_mock.add_expected_print("Сеанс завершён.")

    application.exec()
    console_mock.check_all_mocks_used()

    assert hospital == expected_hospital, "После выполнения команд состояние больницы не соответствует ожидаемому"


def test_non_existent_command():
    console_mock = ConsoleMock()
    hospital = Hospital(
        [Patient(1, 1)]
    )
    expected_hospital = Hospital(
        [Patient(1, 1)]
    )
    application = Application(console_mock, hospital)
    console_mock.add_expected_input(expected_text="Введите команду", expected_input="выписать всех пациентов")
    console_mock.add_expected_print(print_text="Неизвестная команда! Попробуйте ещё раз")

    console_mock.add_expected_input("Введите команду", "стоп")
    console_mock.add_expected_print("Сеанс завершён.")

    application.exec()
    console_mock.check_all_mocks_used()

    assert hospital == expected_hospital


@pytest.mark.parametrize(
    "wrong_id", ("два", "1,2", "1.2")
)
def test_wrong_patient_id(wrong_id):
    console_mock = ConsoleMock()
    hospital = Hospital(
        [Patient(1, 1)]
    )
    expected_hospital = Hospital(
        [Patient(1, 1)]
    )
    application = Application(console_mock, hospital)
    console_mock.add_expected_input(expected_text="Введите команду", expected_input="status up")
    console_mock.add_expected_input("Введите ID пациента", wrong_id)
    console_mock.add_expected_print(print_text="Ошибка ввода. ID пациента должно быть числом (целым, положительным)")

    console_mock.add_expected_input("Введите команду", "стоп")
    console_mock.add_expected_print("Сеанс завершён.")

    application.exec()
    console_mock.check_all_mocks_used()

    assert hospital == expected_hospital