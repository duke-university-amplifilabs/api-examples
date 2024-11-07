from client import DukeApi
from schemas.measures import MeasureCategory, MeasureLevel


def main():
    duke_api = DukeApi()
    measures = duke_api.list_measures(
        category=MeasureCategory.DEMOGRAPHICS, level=MeasureLevel.TRACT
    )
    print("Available measures: ", measures)


if __name__ == "__main__":
    main()
