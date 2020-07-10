# load in the pandas library and rename it as pd
import pandas as pd

# read the file (csv)
""" 'filename' -> dataframe """
df = pd.read_csv("./Resources/Raw/Raw_Assessments_as_CSV.csv")
# note "\" is a special character in python, and paths can be affected

""" reference columns """
# columns_names = [
#     'Person Id', 'First Name', 'Last Name', 'Full Name', 'Active CM?',
#     'Corps Year', 'Ethnicity', 'Person of Color', 'Current Institute', 'Current Region',
#     'Primary Coach', 'School Name', 'School Director', 'Institute Collab ID', 'Class/Subject ID',
#     'Class/Subject Description', 'Grade', 'Subject', 'Subject Modifier',
#     'Assessment Id', 'Assessment Type', 'Assessment Status', 'Date of Assessment',
#     'Assessment Name for % BA', 'Assessment Scale', 'Class Average', 'Number of Students',
#     'Teacher Impact Goal', 'Student Attainment Goal'
# ]

# Step 1
""" 
MAP the dataframe to hold on to the only columns
that you would like to keep
"""

""" static column removal - easiest to understand """
# df.drop('First Name', 1)
# df.drop('Last Name', 1)
""" etc. 
Not ideal for programming because it involves a lot of copy paste
and can lead to replicated errors in the code + hard to debug.
"""

""" dynamic column removal - easiest to implement if you understand looping """
# create a list of the columns you would like to remove
columns_to_drop = [
    'First Name', 'Last Name', 'Active CM?', 'Ethnicity',
    'School Director', 'Institute Collab ID',
    'Class/Subject Description', 'Subject Modifier'
]
# write your for loop to iterate over the columns
# to remove and drop those columns from the dataframe
for column in columns_to_drop:
    df.drop(column, 1)

""" rename assessment name column for easier reading
'Assessment Name for % BA' -> 'Assessment Name'
"""
# rename column
# note: we are reassigning df to have the new dataframe
df = df.rename(columns={'Assessment Name for % BA': 'Assessment Name'})

# Step 2
"""
FILTER for valid assessments
"""
# create a collection of assessment names
# this was copy pasted from the csv
assessments_to_keep = [
    'SC EOCEP, Biology 1/Applied Biology 2',
    'SMI: Scholastic Math Inventory',
    'NWEA Math -Measures of Academic Progress-grades 3-HS',
    'NWEA Reading -Measures of Academic Progress-grades 3-HS',
    'STAR Math (Renaissance)',
    'NWEA Language Usage -Measures of Academic Progress-grades 3-HS',
    'NWEA Reading- Measures of Academic Progress- Primary Grades',
    'NWEA Math- Measures of Academic Progress- Primary Grades',
    'SC EOCEP, English 1',
    'SRI: Scholastic Reading Inventory',
    'STAR Reading (Renaissance)',
    'ACT English'
]
# create new dataframe with only valid assessments
# this uses the pandas.Dataframe.isin method for the filter value
df_valid_asmt = df[df['Assessment Name'].isin(assessments_to_keep)]
