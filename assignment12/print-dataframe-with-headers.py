# Task 5

import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    # This prints the DataFrame with headers every 10 rows
    def print_with_headers(self):
        total_rows = len(self)
        start = 0

        while start < total_rows:
            end = start + 10
            # Print a chunk of 10 rows
            print("\n", self.iloc[start:end])
            start = end


# Load the products.csv into a DFPlus object
dfp = DFPlus.from_csv("./csv/products.csv")

# Print the DataFrame with headers every 10 rows
dfp.print_with_headers()