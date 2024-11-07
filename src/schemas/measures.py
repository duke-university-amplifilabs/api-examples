from enum import Enum


class MeasureCategory(str, Enum):
    DEMOGRAPHICS = "demographics"
    INDICES = "indices"
    ECONOMY = "economy"
    INFRASTRUCTURE = "infrastructure"
    HEALTH = "health"
    EDUCATION = "education"
    ENVIRONMENT = "environment"
    HOUSING = "housing"


class MeasureLevel(str, Enum):
    BLOCK_GROUP = "block_group"
    TRACT = "tract"
