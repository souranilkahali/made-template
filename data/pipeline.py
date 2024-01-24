import sqlite3
import pandas as pd
#1st data source

# Read data from the excel file
csv_file_path1 = r"D:\Documents\MS_COURSES\MADE\Northern Hemisphere-mean monthly, seasonal, and annual means.csv"
df1 = pd.read_csv(csv_file_path1, sep=";", on_bad_lines='skip')

#2nd data source

# Read data from the excel file
csv_file_path2 = r"D:\Documents\MS_COURSES\MADE\Southern Hemisphere-mean monthly, seasonal, and annual means.csv"
df2 = pd.read_csv(csv_file_path2, sep=";", on_bad_lines='skip')

#3rd data source

# Read data from the excel file
csv_file_path2 = r"D:\Documents\MS_COURSES\MADE\sealevel.csv"
df3 = pd.read_csv(csv_file_path2, sep=",", on_bad_lines='skip')

# Create a connection to the SQLite database
db_file_path = r"D:\Documents\MS_COURSES\MADE\made-template\data\autopipeline.sqlite"
conn = sqlite3.connect(db_file_path)

# Write the DataFrame to a new table in the SQLite database
table_name1 = "Northern Hemisphere-Combined Land-Surface Air and Sea-Surface Water Temperature Anomalies"
df1.to_sql(table_name1, conn, if_exists="replace", index=False)

table_name2 = "Southern Hemisphere-Combined Land-Surface Air and Sea-Surface Water Temperature Anomalies"
df2.to_sql(table_name2, conn, if_exists="replace", index=False)

table_name3 = "Change in sea level"
df3.to_sql(table_name3, conn, if_exists="replace", index=False)

# Close the database connection
conn.close()