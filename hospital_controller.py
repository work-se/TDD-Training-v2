from communication_controller import CommunicationController
from hospital import Hospital


class HospitalController:

    def __init__(self, hospital=None, communication_controller=None):
        self._communication_controller = (
            communication_controller if communication_controller is not None else CommunicationController()
        )
        self._hospital = hospital if hospital is not None else Hospital()

