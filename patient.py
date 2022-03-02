class Patient:

    def __init__(self, patient_id, status):
        self._patient_id = patient_id
        self._status = status

    def get_status(self) -> int:
        return self._status

    def status_up(self):
        self._status += 1

    def status_down(self):
        self._status -= 1
