from communication_controller import CommunicationController, CommandTypes, InputWrongPatientId


class Application:

    def __init__(self, communication_controller=None, hospital=None):
        self._communication_controller = (
            communication_controller if communication_controller is not None else CommunicationController()
        )
        self._hospital = hospital

    def exec(self):
        while True:
            command = self._communication_controller.get_command()
            if command is None:
                continue

            if command == CommandTypes.STOP:
                self._communication_controller.print_stop_session()
                break
            elif command == CommandTypes.STATUS_UP:
                try:
                    patient_id = self._communication_controller.get_patient_id()
                except InputWrongPatientId as exception:
                    self._communication_controller.print_exception()
