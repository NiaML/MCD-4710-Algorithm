# Name: Chi Him Lam
# Student ID: 33191654
# Assignment 1 - T2 2022

# Add your code below the test cases provided in each function
# Task 1
def read_data(filename):
    """
    Input: The name of the data file (filename)
    Output: A table with data in the given file. 

    For example:
    >>> patient_data = read_data('hospital_data.csv')
    >>> patient_data[:3] # The first three rows of the table
    [['SMITH', 'M', 38.0, 176.0, 145.0, 1, 124.0, 93.0], ['JOHNSON', 'M', 43.0, 163.0, 146.0, 0, 109.0, 77.0], ['WILLIAMS', 'F', 38.0, 131.0, 147.0, 0, 125.0, 83.0]]
    """
    # Add your code here

    

# Task 2
def lbs_to_kg(table):
    """
    Input: A table containing all the patient data that is available in the give data file.
    Output: The table with weight converted to kilograms

    For example:
    >>> patient_data = read_data('hospital_data.csv')
    >>> lbs_to_kg(patient_data)
    >>> patient_data[:3] # The first three rows of the modified table
    [['SMITH', 'M', 38.0, 79.8, 145.0, 1, 124.0, 93.0], ['JOHNSON', 'M', 43.0, 73.9, 146.0, 0, 109.0, 77.0], ['WILLIAMS', 'F', 38.0, 59.4, 147.0, 0, 125.0, 83.0]]

    """
    # Add your code here

    

# Task 3
def calculate_BMI(table):
    """
    Input: A table containing all the patient data that is available in the give data file, with the weight converted to kg.
    Output: The table with the BMI values added to the last column of the table.

    For example: 
    >>> patient_data = read_data('hospital_data.csv')
    >>> lbs_to_kg(patient_data)
    >>> calculate_BMI(patient_data)
    >>> patient_data[:3] # The first three rows of the modified table
    [['SMITH', 'M', 38.0, 79.8, 145.0, 1, 124.0, 93.0, 38.0], ['JOHNSON', 'M', 43.0, 73.9, 146.0, 0, 109.0, 77.0, 34.7], ['WILLIAMS', 'F', 38.0, 59.4, 147.0, 0, 125.0, 83.0, 27.5]]
    """
    # Add your code here

    

# Task 4
def categorise(table):
    """
    Input: A table containing all the patient data that is available in the give data file, with the BMI values appended.
    Output: The table with the categories added to the last column of the table.

    For example: 
    >>> patient_data = read_data('hospital_data.csv')
    >>> lbs_to_kg(patient_data)
    >>> calculate_BMI(patient_data)
    >>> categorise(patient_data)
    >>> patient_data[:3] # The first three rows of the modified table
    [['SMITH', 'M', 38.0, 79.8, 145.0, 1, 124.0, 93.0, 38.0, 'O'], ['JOHNSON', 'M', 43.0, 73.9, 146.0, 0, 109.0, 77.0, 34.7, 'O'], ['WILLIAMS', 'F', 38.0, 59.4, 147.0, 0, 125.0, 83.0, 27.5, 'N']]
    """
    # Add your code here

    

# Task 5
def get_BMI(table,name):
    """
    Input: A table containing all the patient data that is available in the give data file, with the BMI values appended and the name of a patient.
    Output: The BMI value of the given patient.

    For example: 
    >>> patient_data = read_data('hospital_data.csv')
    >>> lbs_to_kg(patient_data)
    >>> calculate_BMI(patient_data)
    >>> get_BMI(patient_data,'Johnson')
    34.7
    """
    # Add your code here

    

# Task 6
def get_BP(table,name):
    """
    Input: A table containing all the patient data that is available in the give data file and the name of a patient.
    Output: The blood pressure readings of the given patient as a tuple.

    For example: 
    >>> patient_data = read_data('hospital_data.csv')
    >>> get_BP(patient_data,'Johnson')
    (109, 77)
    """
    # Add your code here

    

# Task 7
def is_smoker(table,name):
    """
    Input: A table containing all the patient data that is available in 
    the give data file and the name of a patient.
    Output: True if the patient is a smoker and False otherwise.

    For example: 
    >>> patient_data = read_data('hospital_data.csv')
    >>> is_smoker(patient_data,'Johnson')
    False
    >>> is_smoker(patient_data,'White')
    True
    """
    # Add your code here

    

# Task 8
def extract_high_risk(table,filename):
    """
    Input: A table containing all the patient data and a filename
    Output: The given file updated with the high-risk patient details

    For example: 
    >>> patient_data = read_data('hospital_data.csv')
    >>> lbs_to_kg(patient_data)
    >>> calculate_BMI(patient_data)
    >>> categorise(patient_data)
    >>> extract_high_risk(patient_data,'high_risk_patients.csv')
    >>> high_risk_table = read_data('high_risk_patients.csv') # read high-risk values (for testing)
    >>> high_risk_table[:2] # The first two rows of the high-risk records
    [['SMITH', 'M', 38.0, 79.8, 145.0, 1, 124.0, 93.0, 38.0, 'O'], ['WHITE', 'M', 39.0, 91.6, 152.0, 1, 130.0, 95.0, 39.6, 'O']]

    """
    # Add your code here
    
    
            
            
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


