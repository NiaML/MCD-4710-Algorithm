# Name: Chi Him Lam
# Student ID: 33191654

# Template for Assignment 1 - T2 2022
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
    # read data from the file and store at variable patient_data
    f = open(filename, 'r')
    patient_data = f.read().splitlines()
    f.close()

    # remove the first line of the file as it is the header
    patient_data.pop(0)

    # convert the data into a table
    patient_data = [line.split(',') for line in patient_data]
    
    # set the values to be floats if they are to be read as numerical values
    for row in range(len(patient_data)):
        for col in range(len(patient_data[row])):
            
            if patient_data[row][col][0].isalpha() == False:
                patient_data[row][col] = float(patient_data[row][col])
                
    
    # set the smoker column to be integers or booleans in another way
    for row in range(len(patient_data)):
        patient_data[row][5] = int(patient_data[row][5])
    
    
    return patient_data

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
    # apply the scaling factor 1:0.4536 to the table
    lbs_to_kg_scale = 0.4536
    for row in range(len(table)):
        lbs = table[row][3]
        kg = lbs * lbs_to_kg_scale
        table[row][3] = round(kg, 1)

    

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
    # the code below that is commented out is because it makes the function to be working exculsively fine in this scene
    # # safe check if the table has converted the weight to kg
    # temp_data = read_data('hospital_data.csv')
    # if not table[0][3] == lbs_to_kg(temp_data[0][3]):
    #     lbs_to_kg(table)
    # del temp_data
    

    # calculate the BMI value and add it to the end of each row in table
    for row in range(len(table)):
        # break down the data into variables for readability
        mass    = table[row][3]
        height  = table[row][4] / 100 # convert the height to meters
        BMI     = round(mass / (height ** 2), 1)
        table[row].append(BMI)
    return table

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
    # determine the category of the BMI value and add it to the end of each row in table
    # declare the categories
    categories = {  
                'Obese':"O", 
                'Normal':'N', 
                'Underweight':'U'
                }
    for row in range(len(table)):
        BMI = table[row][-1]
        if BMI < 18:
            table[row].append(categories['Underweight'])
        elif 18<=BMI and BMI<30:
            table[row].append(categories['Normal'])
        elif BMI >= 30:
            table[row].append(categories['Obese'])
    return table

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
    # find the row of the given patient
    # this method only display the first patient with the given name
    for row in range(len(table)):
        if table[row][0] == name.upper(): # the given name list is in upper case
            BMI = table[row][-1]
            return BMI
    return None
    # further improvement: 
    # find all the patients with the given name
    # return a list of all the BMI values of the given name

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
    # reuse of the lookup method but return of different data
    for row in range(len(table)):
        if table[row][0] == name.upper(): # the given name list is in upper case
            systolic    = int(table[row][6])
            diastolic   = int(table[row][7])
            return (systolic, diastolic)
    return None

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
    # reuse of the lookup method but return of different data
    for row in range(len(table)):
        if table[row][0] == name.upper(): # the given name list is in upper case
            smoker    = bool(table[row][5])
            
            return smoker
    return None

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
    # test all conditions and write the high-risk patient details to the given file
    categories = {  
                'Obese':"O", 
                'Normal':'N', 
                'Underweight':'U'
                }
    file = open(filename, 'w')
    patient_row = 0
    while patient_row < len(table):
        # get all the data required for the high-risk patient
        patient_name    = table[patient_row][0]
        patient_BMI     = get_BMI(table,patient_name)
        patient_BP      = get_BP(table,patient_name)
        patient_smoker  = is_smoker(table,patient_name)
        # test the conditions, convertible to nested if statements to avoid stacking in one line
        if patient_BMI == categories['Obese'] and patient_BP[0] > 125 and patient_BP[1]>=85 and patient_smoker:
            patient_info = ''
            for col in range(len(table[patient_row])):
                patient_info += str(table[patient_row][col]) + ','
            patient_info = patient_info[:-1] + '\n'
            # write the high-risk patient details to the given file
            file.write(patient_info)
        patient_row += 1
    file.close()

patient_data = read_data('hospital_data.csv')
lbs_to_kg(patient_data)
calculate_BMI(patient_data)
categorise(patient_data)
extract_high_risk(patient_data,'high_risk_patients.csv')
high_risk_table = read_data('high_risk_patients.csv') # read high-risk values (for testing)
temp = high_risk_table[:2] # The first two rows of the high-risk records
    # [['SMITH', 'M', 38.0, 79.8, 145.0, 1, 124.0, 93.0, 38.0, 'O'], ['WHITE', 'M', 39.0, 91.6, 152.0, 1, 130.0, 95.0, 39.6, 'O']]
  
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


