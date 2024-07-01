# LazyExecutionDataFrame

LazyExecutionDataFrame is a Python library designed to replicate the behavior of PySpark DataFrame, specifically focusing on lazy evaluation. In this model, data processing is postponed until the data is explicitly required, such as during display or write operations. This means that operations like select, where, join, and groupBy are not executed immediately but only when the data is actually needed.

The library is developed as part of a larger project intended to serve as a mock for unit testing PySpark applications. It is not intended for standalone use, as its primary focus is not on performance or efficiency but on accurately mimicking PySpark's behavior.
