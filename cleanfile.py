import pandas as pd

# Load the CSV file
df = pd.read_csv('cust_data.csv')

# Remove non-numeric characters from the phone column
df['phone'] = df['phone'].str.replace(r'\D', '', regex=True)  # Removes anything that's not a number

# Now save the cleaned file to a new CSV
df.to_csv('cleancust_data123.csv', index=False)
