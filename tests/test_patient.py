import pytest

from patient import Patient


def test_get_status():
    patient = Patient(1, 2)
    assert patient.get_status() == 2, "Неверный статус пациента"


def test_status_up():
    patient = Patient(1, 2)
    patient.status_up()
    assert patient._status == 3, "Неверный статус пациента после повышения"


def test_status_down():
    patient = Patient(1, 2)
    patient.status_down()
    assert patient._status == 1, "Неверный статус пациента после понижения"
