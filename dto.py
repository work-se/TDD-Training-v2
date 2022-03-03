from dataclasses import dataclass


@dataclass(frozen=True)
class StatisticsPartDto:
    status: str
    patients_number: int

    def __eq__(self, other: 'StatisticsPartDto') -> bool:
        return self.status == other.status and self.patients_number == other.patients_number
