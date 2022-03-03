from communication_controller import CommunicationController, InputWrongPatientId
from hospital import Hospital


class HospitalController:

    def __init__(self, hospital=None, communication_controller=None):
        self._communication_controller = (
            communication_controller if communication_controller is not None else CommunicationController()
        )
        self._hospital = hospital if hospital is not None else Hospital()

    def patient_status_up(self):
        try:
            patient_id = self._communication_controller.get_patient_id()
            self._hospital.patient_status_up(patient_id)
            new_status = self._hospital.get_patient_status(patient_id)
            self._communication_controller.print_new_patient_status(new_status)
        except InputWrongPatientId as exception:
            self._communication_controller.print_exception(str(exception))

    def patient_status_down(self):
        try:
            patient_id = self._communication_controller.get_patient_id()
            self._hospital.patient_status_down(patient_id)
            new_status = self._hospital.get_patient_status(patient_id)
            self._communication_controller.print_new_patient_status(new_status)
        except InputWrongPatientId as exception:
            self._communication_controller.print_exception(str(exception))

    def get_patient_status(self):
        try:
            patient_id = self._communication_controller.get_patient_id()
            status = self._hospital.get_patient_status(patient_id)
            self._communication_controller.print_current_patient_status(status)
        except InputWrongPatientId as exception:
            self._communication_controller.print_exception(str(exception))

    def print_statistics(self):
        statistics = list(filter(
            lambda item: item.patients_number > 0, self._hospital.get_statistics()
        ))
        self._communication_controller.print_statistics(statistics)
