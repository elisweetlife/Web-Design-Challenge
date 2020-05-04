import pandas as pd

cities = pd.read_csv("WebVisualizations/cities.csv")
cities.to_html("dataTable.html", index=False, classes=["table"])


