import pytest

from patient import Patient


def test_get_status():
    patient = Patient(1, 2)
    assert patient.get_status() == 2, "Неверный статус пациента"


def test_status_up():
    patient = Patient(1, 2)
    patient.status_up()
    assert patient.status == 3, "Неверный статус пациента после повышения"


def test_status_down():
    patient = Patient(1, 2)
    patient.status_down()
    assert patient.status == 1, "Неверный статус пациента после понижения"


def test_compare_patients():
    equal_patient1 = Patient(1, 2)
    equal_patient2 = Patient(1, 2)
    assert equal_patient1 == equal_patient2, "Сравнение пациентов работает неверно"

    different_id_patient1 = Patient(1, 2)
    different_id_patient2 = Patient(2, 2)
    assert different_id_patient1 != different_id_patient2, "Сравнение пациентов работает неверно"

    different_status_patient1 = Patient(1, 2)
    different_status_patient2 = Patient(2, 2)
    assert different_status_patient1 != different_status_patient2, "Сравнение пациентов работает неверно"

