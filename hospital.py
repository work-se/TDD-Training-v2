from patient import Patient


class Hospital:
    STATUSES = {
        0: "Тяжело болен",
        1: "Болен",
        2: "Слегка болен",
        3: "Готов к выписке"
    }

    def __init__(self, patients):
        self._form_hospital(patients)

    def _form_hospital(self, patients):
        self._patient_idx = 0
        self._patients = {}
        for patient in patients:
            self._patients[patient.patient_id] = patient
            if patient.patient_id > self._patient_idx:
                self._patient_idx = patient.patient_id

    def add_patient(self, status: int):
        self._patient_idx += 1
        self._patients[self._patient_idx] = Patient(self._patient_idx, status)

    def get_patient_status(self, patient_id: int):
        status_id = self._patients[patient_id].get_status()
        return self.STATUSES[status_id]

    def patient_status_up(self, patient_id: int):
        self._patients[patient_id].status_up()

    def patient_status_down(self, patient_id: int):
        self._patients[patient_id].status_down()

    def __eq__(self, other: 'Hospital') -> bool:
        return self._patients == other._patients and self._patient_idx == other._patient_idx
