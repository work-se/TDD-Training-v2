from communication_controller import CommunicationController, CommandTypes, InputWrongPatientId
from hospital_controller import HospitalController


class Application:

    def __init__(self, communication_controller=None, hospital_controller=None):
        self._communication_controller = (
            communication_controller if communication_controller is not None else CommunicationController()
        )
        self._hospital_controller = hospital_controller if hospital_controller is not None else HospitalController()

    def exec(self):
        while True:
            command = self._communication_controller.get_command()
            if command is None:
                continue

            if command == CommandTypes.STOP:
                self._communication_controller.print_stop_session()
                break
            elif command == CommandTypes.STATUS_UP:
                self._hospital_controller.patient_status_up()
