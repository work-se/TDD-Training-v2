class Patient:

    def __init__(self, patient_id, status):
        self.patient_id = patient_id
        self.status = status

    def get_status(self) -> int:
        return self.status

    def status_up(self):
        self.status += 1

    def status_down(self):
        self.status -= 1

    def __eq__(self, other: 'Patient') -> bool:
        return self.patient_id == other.patient_id and self.status == other.status

    def __repr__(self):
        return f"[Patient] (id={self.patient_id}, status={self.status})"

    def __str__(self):
        return f"[Patient] (id={self.patient_id}, status={self.status})"
