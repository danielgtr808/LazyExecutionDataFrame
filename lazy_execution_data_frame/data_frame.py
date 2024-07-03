from typing import List


class DataFrame():
    
    def __init__(self, headers: List, body: List[List]) -> None:
        self.headers = headers
        self.body = body


    def show(self, n = 20, truncate = True) -> List[str]:
        rows = [self.headers, *self.body[:n]]
        characters_per_column: List[int] = []
        
        if (truncate):
            characters_per_column = [20 for x in self.headers]
        else:
            characters_per_column = [
                max(map(lambda x: len(x[i]), rows))
                for i, y in
                enumerate(self.headers)
            ]

        delimiter_row = "+" + "+".join(["-"*x for x in characters_per_column]) + "+"

        rows_to_print = List = [delimiter_row]
        for row in rows:
            row_to_print: List = []
            for column_number, column_length in enumerate(characters_per_column):
                row_to_print.append(
                    f"{row[column_number][:column_length-3]}..."
                    if (len(row[column_number]) > column_length) else
                    row[column_number].rjust(column_length, " ")
                )

            rows_to_print.append("|" + "|".join(row_to_print) + "|")

        rows_to_print.insert(2, delimiter_row)
        rows_to_print.append(delimiter_row)

        for x in rows_to_print:
            print(x)

        return rows_to_print
