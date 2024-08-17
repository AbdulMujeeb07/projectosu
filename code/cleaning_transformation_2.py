# Reading the Scraped Dataset
import pandas as pd
df_all = pd.read_csv("C:\\Users\\thepo\\Documents\\GitHub\\project-deliverable-2-red-hot-stilly-peppers\\data\\Masterlist_dv1.csv", encoding='unicode_escape')
df_all
print(df_all.dtypes)
# Removing the extra words like "Miles", "Mins" etc
import regex
df_all['Time taken by car'] = df_all['Time taken by car'].str.replace(r'Min|s','')    # Removing the word "Min|Mins" from Time Taken Column
df_all['Time taken by walk'] = df_all['Time taken by walk'].str.replace(r'Min|s','')# Removing the word "Min|Mins" from Time Taken Column
df_all['Distance by walk'] = df_all['Distance by walk'].str.replace(r'Mile|s','')
df_all['Distance by vehicle'] = df_all['Distance by vehicle'].str.replace(r'Mile|s','')
df_all

df_all['Time taken by car'] = pd.to_numeric(df_all['Time taken by car'], errors='coerce')   # Converting to int/float
df_all['Time taken by walk'] = pd.to_numeric(df_all['Time taken by walk'], errors='coerce')    # Converting to int/float
df_all['Distance by walk'] = pd.to_numeric(df_all['Distance by walk'], errors='coerce')    # Converting to int/float
df_all['Distance by vehicle'] = pd.to_numeric(df_all['Distance by vehicle'], errors='coerce')    # Converting to int/float
df_all['sqft'] = pd.to_numeric(df_all['sqft'], errors='coerce')    # Converting to int/float
df_all['Rent'] = pd.to_numeric(df_all['Rent'], errors='coerce')# Converting to int/float
df_all['Cost Per Person'] = pd.to_numeric(df_all['Cost Per Person'], errors='coerce')
print(df_all.dtypes)    # Checking Datatype
df_all

# Transforming missing values
df_all['sqft']
df_all = df_all.drop('Unnamed: 0', axis=1)
df_sqft_5 = df_all[(df_all['Beds'] == 5) & ((df_all['Baths'] == 3)|(df_all['Baths'] == 2))]
mean_1 = df_sqft_5['sqft'].mean()
df_all.at[13,'sqft'] = mean_1    # Replacing with mean

# Transorming the missing value for Beds = 3 and baths = 2
df_sqft_3 = df_all[(df_all['Beds'] == 3) & (df_all['Baths'] == 2)]    # Filtering all rows with similar beds and baths
df_sqft_3.dtypes
df_sqft_3.hist(column='sqft')
plt.show()
median_1 = df_sqft_3['sqft'].median()
df_all.at[14,'sqft'] = median_1    # Replacing with median as the data is right skewed

# Transorming the missing value for Beds = 1 and baths = 1
df_sqft_1 = df_all[(df_all['Beds'] == 1) & (df_all['Baths'] == 1)]    # Filtering all rows with similar beds and baths
df_sqft_1
df_sqft_1.hist(column='sqft')
plt.show()
median_2 = df_sqft_1['sqft'].median()
df_all.at[167,'sqft'] = median_1    # Replacing with median as the data is right skewed
df_all['sqft']

# Transorming the missing value for Beds = 2 and baths = 1
df_sqft_2 = df_all[(df_all['Beds'] == 2) & (df_all['Baths'] == 1)]    # Filtering all rows with similar beds and baths
df_sqft_2
df_sqft_2.hist(column='sqft')
plt.show()
mean_2 = df_sqft_2['sqft'].mean()
df_all.at[168,'sqft'] = mean_2    # Replacing with median as the data is right skewed
df_all['sqft']

# Transformation for Rent - Finding filtered dataset and replacing values
df_1 = df_all[(df_all['Beds'] == 1) & (df_all['Baths'] == 1)]    # Filtering all rows with similar beds and baths
df_1
df_1.hist(column='Cost Per Person')
plt.show()
med_1 = df_1['Cost Per Person'].median()
df_all.at[34,'Rent'] = med_1    # Replacing with median as the data is right skewed
df_all.at[34,'Cost Per Person'] = med_1

# Transforming for Rent
df_2 = df_all[(df_all['Beds'] == 2) & (df_all['Baths'] == 2)]    # Filtering all rows with similar beds and baths
df_2
df_2.hist(column='Cost Per Person')
plt.show()
med_2 = df_2['Cost Per Person'].median()
df_all.at[35,'Rent'] = med_2    # Replacing with median as the data is right skewed
df_all.at[35,'Cost Per Person'] = med_2
df_all.at[36,'Rent'] = med_2    # Replacing with median as the data is right skewed
df_all.at[36,'Cost Per Person'] = med_2
df_all.at[37,'Rent'] = med_2    # Replacing with median as the data is right skewed
df_all.at[37,'Cost Per Person'] = med_2
df_all.at[38,'Rent'] = med_2    # Replacing with median as the data is right skewed
df_all.at[38,'Cost Per Person'] = med_2

# 3 beds 3 baths
df_3 = df_all[(df_all['Beds'] == 3) & (df_all['Baths'] == 3)]    # Filtering all rows with similar beds and baths
df_3
df_3.hist(column='Cost Per Person')
plt.show()
mean_3 = df_3['Cost Per Person'].mean()
df_all.at[39,'Rent'] = mean_3    # Replacing with mean
df_all.at[39,'Cost Per Person'] = mean_3
df_all.at[40,'Rent'] = mean_3    # Replacing with mean as there is only one value
df_all.at[40,'Cost Per Person'] = mean_3

df_all.to_csv("C:\\Users\\thepo\\Documents\\GitHub\\project-deliverable-2-red-hot-stilly-peppers\\data\\Cleaned_Data_dv_2.csv")