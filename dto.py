from dataclasses import dataclass


@dataclass(frozen=True)
class StatisticsPartDto:
    status: str
    patients_number: int
