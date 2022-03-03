import pytest

from patient import Patient
from hospital import Hospital


def test_form_patients():
    hospital = Hospital([Patient(1, 2), Patient(3, 2)])
    expected_formed_patients = {
        1: Patient(1, 2),
        3: Patient(3, 2)
    }
    assert hospital._patients == expected_formed_patients, "При создании Hospital сформирован неверный объект пациентов"
    assert hospital._patient_idx == 3, "Неверный индекс пациентов"


def test_add_patient():
    hospital = Hospital([])
    expected_patients = {
        1: Patient(1, 2)
    }

    hospital.add_patient(status=2)
    assert hospital._patient_idx == 1, "Неверное количество пациентов после добавления"
    assert hospital._patients == expected_patients, "Сформированные пациенты не соответствуют ожидаемым"


def test_patient_status_up():
    hospital = Hospital([Patient(1, 2), Patient(2, 2)])
    expected_patients = {
        1: Patient(1, 3),
        2: Patient(2, 2)
    }
    hospital.patient_status_up(1)
    assert hospital._patients == expected_patients, "Статус пациента не изменился"


def test_patient_status_down():
    hospital = Hospital([Patient(1, 2), Patient(2, 2)])
    expected_patients = {
        1: Patient(1, 1),
        2: Patient(2, 2)
    }
    hospital.patient_status_down(1)
    assert hospital._patients == expected_patients, "Статус пациента не изменился"


def test_get_patient_status():
    hospital = Hospital([Patient(1, 2)])
    status = hospital.get_patient_status(1)
    assert status == "Слегка болен", "Получен неверный статус пациента"