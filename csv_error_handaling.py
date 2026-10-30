import pandas as pd
try:
    data = pd.read_csv('data.csv')
except FileNotFoundError:
    print("Error: The file 'data.csv' was not found.")

except pd.errors.EmptyDataError:
    print("Error: The file 'data.csv' is empty.")

except PermissionError:
    print("Error: Permission denied while trying to read 'data.csv'.")

else:
    print("Data loaded successfully:")
    print(data.head())

finally:
    print("CSV loading completed.")