from typing import List
from .data_frame import DataFrame

import csv



class DataFrameReader():
    pass

    def csv(self, path: str, delimiter: str = ",", header: bool = True) -> DataFrame:
        with open(path) as file_reference:
            csv_reader = csv.reader(
                file_reference,
                delimiter = delimiter
            )

            header_row: List = []
            if (header):
                for row in csv_reader:
                    header_row = row
                    break

            body = list(csv_reader)
            if (not header):
                for i in range(max(map(lambda x: len(x), body))):
                    header_row.append(f"_{i}")

            return DataFrame(header_row, body)
            