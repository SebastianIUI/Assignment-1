import pandas as pd

# Load the CSV file
df = pd.read_csv(r'c:\Users\sebas\Downloads\TV_show_data (2).csv')

# Count columns with string (object) dtype
string_columns = df.select_dtypes(include=['object']).columns
print(f"Number of columns containing string values: {len(string_columns)}")
print("Columns:", list(string_columns))

