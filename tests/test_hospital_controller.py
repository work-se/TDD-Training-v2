import pytest

from unittest.mock import MagicMock

from communication_controller import InputWrongPatientId
from hospital_controller import HospitalController


def test_patient_status_up():
    hospital = MagicMock()
    communication_controller = MagicMock()
    hospital_controller = HospitalController(hospital, communication_controller)

    communication_controller.get_patient_id = MagicMock(return_value=1)
    hospital.patient_status_up = MagicMock()
    hospital.get_patient_status = MagicMock(return_value="Болен")
    communication_controller.print_new_patient_status = MagicMock()

    hospital_controller.patient_status_up()

    communication_controller.get_patient_id.assert_called()
    hospital.patient_status_up.assert_called_with(1)
    hospital.get_patient_status.assert_called_with(1)
    communication_controller.print_new_patient_status.assert_called_with("Болен")


def test_patient_status_up_with_wrong_id():
    hospital = MagicMock()
    communication_controller = MagicMock()
    hospital_controller = HospitalController(hospital, communication_controller)

    # will be called
    communication_controller.get_patient_id = MagicMock(side_effect=InputWrongPatientId)
    communication_controller.print_exception = MagicMock()

    # will not be called
    hospital.patient_status_up = MagicMock()

    hospital_controller.patient_status_up()

    communication_controller.get_patient_id.assert_called()
    hospital.patient_status_up.assert_not_called()
    communication_controller.print_exception.assert_called_with(
        "Ошибка ввода. ID пациента должно быть числом (целым, положительным)"
    )
