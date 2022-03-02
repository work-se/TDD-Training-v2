import pytest

from unittest.mock import MagicMock

from hospital_controller import HospitalController
from tests.mocks.console_mock import ConsoleMock


def test_get_patient_status():
    hospital = MagicMock()
    communication_controller = MagicMock()

    hospital_controller = HospitalController(hospital, communication_controller)

    hospital_controller.get_patient_status()
