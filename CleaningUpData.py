# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 15:20:48 2025

@author: shalika
"""

# Clean and organize raw sales data (Excel/CSV format).

import csv
import os
#OPEN THE FOLDER AND THEN USE FOR LOOP TO READ
folder = r"C:/Users/shali/OneDrive/Desktop/vs programs/I Business Sales Dashboard/Data"
empty_found = False

#1.incomplete data check
# ITERATIVELY READING THE FILES
for file in os.listdir(folder):
    if file.endswith(".csv"):
        file_path = os.path.join(folder,file)
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)

            for row in reader:
                if "" in row:
                    print(f"Empty cells found in the {file}: {row}")
                    empty_found = True
if not empty_found:
    print("No empty cells\n")

# """NOT DONE BECUASE IT WOULD NOT GIVE ACCURATE RESULTS DURING ANALYSIS
# # #2.noisy data check (use density-based clustering)
# # import pandas as pd
# # df = pd.read_csv(r"C:\Users\shali\OneDrive\Desktop\vs programs\I Business Sales Dashboard\Data\superstore.csv", encoding = "Windows-1252")

# # from sklearn.cluster import DBSCAN
# # from sklearn.preprocessing import StandardScaler
# # X = df.select_dtypes(include=['float64','int64']) #create the dataframe using pandas
# # scaled = StandardScaler().fit_transform(X) 
# # db = DBSCAN(eps=0.5, min_samples=5)
# # df['noise']=db.fit_predict(scaled)
# # noisyrows = df[df['noise'] == -1] #as noise points will have the label value as -1
# # print(noisyrows)
# """

#2.inconsistent data check
import pandas as pd

df = pd.read_csv(r"C:/Users/shali/OneDrive/Desktop/vs programs/I Business Sales Dashboard/Data/superstore.csv", encoding = "Windows-1252")
# fixing datetime columns
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y")  #converting columns to datetime
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d/%m/%Y")
print(df.dtypes)
#put if loops to check if the column is numeric, then try converting the values in it to numeric and check which ones fail(then fix it by removing the record or by filling global constant)
numeric_col = df.select_dtypes(include=["int64","float64"]).columns
for col in numeric_col:
    # Coerce: If a value cannot be converted, turn it into NaN instead of raising an error.
    # .isna(): checks which values are NaN
    mismatch_dtype_rows = df[pd.to_numeric(df[col], errors="coerce").isna()]
    if len(mismatch_dtype_rows) > 0:
        print(f"\nInconsistent data is found in the column: {col}")
        print(mismatch_dtype_rows)
    # else:
    #     print("\nRows have consistent data")

#also check for unexpected category values
print(df["Ship Mode"].unique()) #VALID
print(df["Segment"].unique())  #VALID
print(df["Country"].unique())  #VALID
states_in = (df["State"].unique())
states_list =["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia",
"Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts",
"Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico",
"New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina",
"South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"
]
for state in states_in:
    if state not in states_list:
        print(state)
#One invalid valuetype = district of columbia was found, so change it to washington using excel and save the changes
regions_in = (df["Region"].unique())
regions_list = ["North", "South","East","West","Central"]
for region in regions_in:
    if region not in regions_list:
        print(region)

















# Analyze patterns like monthly sales trends, category-wise performance, and customer behavior.
# Build a visually appealing Power BI dashboard with filters and charts.
# Present insights and recommendations as if you were helping a real business.




























