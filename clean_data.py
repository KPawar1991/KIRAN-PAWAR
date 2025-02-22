import pandas as pd

def clean_csv(input_file, output_file):
    try:
        # Read the CSV file
        data = pd.read_csv(input_file)
        print("Original Data:")
        print(data)

        # Remove rows with null values
        cleaned_data = data.dropna()
        print("\nData after removing null values:")
        print(cleaned_data)

        # Remove duplicate rows
        cleaned_data = cleaned_data.drop_duplicates()
        print("\nData after removing duplicates:")
        print(cleaned_data)
        #clear x between phone column
        if 'phone' in cleaned_data.columns:
            cleaned_data['phone']= cleaned_data['phone'].str.replace(r'\D', '', regex=True)
            print("\nData after removing nullX in phone values:")
            print(cleaned_data)
        else :
            print("'phone' COLUMN not found")
        
        # Save cleaned data to a new CSV file
        cleaned_data.to_csv(output_file, index=False)
        print(f"\nCleaned data saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function
input_file = "CRMdetails.csv"  # Input CSV file
output_file = "cleancrmdetails.csv"  # Output cleaned CSV file
clean_csv(input_file, output_file)

