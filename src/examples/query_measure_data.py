from client import DukeApi
from schemas.measures import MeasureCategory, MeasureLevel


def main():
    duke_api = DukeApi()

    states = duke_api.list_states()

    print("Available states: ", states)

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

    measures = duke_api.query(
        category=MeasureCategory.DEMOGRAPHICS,
        level=MeasureLevel.TRACT,
        measures=[measures[0]],
        years=[years[0]],
        states=[states[0].id],
    )

    print("Query result: ", measures)


if __name__ == "__main__":
    main()
