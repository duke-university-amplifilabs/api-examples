from client import DukeApi
from schemas.measures import MeasureCategory, MeasureLevel


def main():
    duke_api = DukeApi()

    measures = duke_api.list_measures(
        category=MeasureCategory.DEMOGRAPHICS, level=MeasureLevel.TRACT
    )

    print("Available measures: ", measures)

    years = duke_api.list_measure_years(
        category=MeasureCategory.DEMOGRAPHICS,
        level=MeasureLevel.TRACT,
        measure=measures[0],
    )
    print("Available years for an metric: ", years)


if __name__ == "__main__":
    main()
