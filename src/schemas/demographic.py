from dataclasses import dataclass


@dataclass
class DemographicData:
    fips: int
    year: int
    demographic_type_primary: str
    demographic_value_primary: str
    demographic_type_secondary: str
    demographic_value_secondary: str
    percent_cont: float
    quartile: int
