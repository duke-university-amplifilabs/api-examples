from client import DukeApi
from schemas.measures import MeasureCategory, MeasureLevel
import pandas as pd


def main():
    duke_api = DukeApi()

    measures = duke_api.query(
        category=MeasureCategory.DEMOGRAPHICS,
        level=MeasureLevel.BLOCK_GROUP,
        measure=["ethnicity_hispanic:percent", "race_black:percent"],
        year=[2020, 2021],
        state=["37", "38"],
    )

    df = pd.DataFrame(measures)

    print("Dataframe: ", df.head(10))


if __name__ == "__main__":
    main()
