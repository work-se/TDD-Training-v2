import pytest

from hospital import Hospital


def test_add_patient():
    hospital = Hospital([])
    expected_patients = {
        1: Patient(1, 2)
    }

    hospital.add_patinet(status=2)
    assert hospital._patients_number == 1, "Неверное количество пациентов после добавления"
    assert hospital._patients == expected_patients, "Сформированные пациенты не соответствуют ожидаемым"
