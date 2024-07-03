from lazy_execution_data_frame import DataFrameReader

DataFrameReader().csv("example.csv", header=False).show(n = 20)