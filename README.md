Data Cleaning Script for Mall Customer Data
Overview
This script performs data cleaning on a raw dataset of mall customer data. The dataset is read from a CSV file, cleaned, and saved as a new cleaned dataset. The script handles missing values, duplicates, and standardizes various columns, ensuring the data is ready for analysis.

Functionality
clean_data()
The function performs the following operations:

1. Reading the Dataset:

    .The raw dataset is loaded from a CSV file (dataset.csv) using pandas.read_csv(). The dataset is assumed to be separated by a pipe (|) delimiter.

2. Column Name Standardization:

    .All column names are stripped of leading/trailing spaces, converted to lowercase, and spaces are replaced with underscores.

3. Basic Information:

     .Prints out basic information about the dataset, including data types and the number of non-null entries using df.info().
      
      .Displays the first few rows of the dataset with df.head().
      
     .Provides a statistical summary of the dataset using df.describe().

4. Missing Values:

     .Displays the count of missing values in each column using df.isnull().sum().
    
     .Drops any rows with missing values using df.dropna().

5. Duplicate Removal:

     .Drops any duplicate rows in the dataset.

6. Gender Standardization:

     .If the gender column exists, the script:
    
     .Converts all entries to lowercase and strips leading/trailing spaces.
    
     .Replaces 'f' with 'female' and 'm' with 'male'.

7. Date Standardization:

      .If the date_joined column exists, the script:
    
      .Strips leading/trailing spaces and converts the column to string format.
    
      .Converts the date to datetime format with the format %d-%m-%Y. Any invalid date formats are coerced into NaT (Not a Time).

8. Age Conversion:
      
      .If the age column exists, the script:
      
      .Converts the age column to numeric, coercing any errors into NaN.
      
      .Changes the type to Int64, which allows for missing values.

9. Saving the Cleaned Data:

      .After all cleaning steps, the cleaned dataset is saved to a new CSV file (cleaned_mall_customer_data.csv).
