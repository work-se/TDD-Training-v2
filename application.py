from communication_controller import CommunicationController


class Application:

    def __init__(self, communication_controller=None, hospital=None):
        self._communication_controller = (
            communication_controller if communication_controller is not None else CommunicationController()
        )
        self.hospital = hospital

    def exec(self):
        while True:
            command = self._communication_controller.get_command()
            if command is None:
                continue
