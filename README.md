# projectosu
# FINDING AFFORDABLE HOMES (RENTALS) FOR STUDENTS AND NON-RESIDENTS IN THE CITY OF STILLWATER

## Executive Summary

The city of Stillwater is home to over fifty thousand people, and students make up over 50% of that. Oklahoma State University sees thousands of students migrating every year to work, study, and grow. Many of these students are thousands of miles from home, in a new country for the first time, having to go through the painful process of finding housing fit to their needs. On top of this, Stillwater is especially prone to Slumlords and overpriced rentals. An article on Oklahoma News 4* from March 2022 is just one of the many cases in Stillwater where the residents of an apartment complex were asked to move out of their homes before the end of the lease term. The inspiration for this project is driven by our personal struggles in finding affordable homes as new residents of Stillwater, while juggling school and financial complications. "Apartment Hunting" is a ubiquious term that automatically triggers a feeling of anxiety in a person's mind because of how daunting the process can be hence, this project aims to ease that process by studying the factors that affect the prices of rentals in the city of Stillwater. Although we might not be able to stop landlords from overcharging their tenants, we sure can help people prioritize their needs by simplyfying choices based on physical and financial constraints. As students of Oklahoma State University, we are always encouraged to help others and what better way to help the society than giving people the happiness of finding affordable and comfortable homes. We seek to understand the driving factors behind rent prices in Stillwater, such as geographic, spatial, and economic variables, and to develop a tool to allow incoming students of next year's MS BAnDS cohort to find adequate living spaces that match their needs.

Citation* [Ogle/KFOR, K. (2022, March 15). Stillwater apartment complex asks tenants to move, residents panicked &amp; confused. KFOR.com Oklahoma City. Retrieved November 6, 2022, from https://kfor.com/news/local/stillwater-apartment-complex-asks-tenants-to-move-residents-panicked-confused/]

## Statement of Scope
To gather data on student-focused residence rentals around Stillwater in order to match students with affordable housing based on a variety of given factors/variables. If we can successfully implement a tool to enable first-time renters in avoiding slum lords, bad contracts, and any number of adverse rental scams, we can establish a report, and start to market the tool.

A) Project Objectives

i) To find the relationship between price of residence rentals and factors (Size, Zones, Amenities, Distance from Oklahoma State University etc.) that influence it.

ii) Based on objective (i), to help tenants prioritize certain factors and match them with affordable homes pertinent to their needs.

Sample: The number of properties up for rent is relatively low mid-way through the fall semester as most landlords have fixed lease terms.The project starts off by scraping information on residence rental listings off marketplace websites (apartmentfinder.com and trulia.com) to cover a diverse set of stand alone (individual) homes and community buildings. 

B) Unit of Analysis

For this project, the Price ($) of apartment rentals will be the most important factor and also our unit of analysis.

## Project Schedule

This project was ideated and finalised for execution in September 2022. The team working on this project has 4 members with niche area of expetise. The members are:
1) Ray Litchfield (Ray) - Data Scraping Specialist
2) Ritwik Roy Chowdhury (Roy) - Data Cleaning Specialist 
3) Chandrika Kompella (Chandrika) - Data Consolidation Specialist
4) Abdul Mujeeb (Abdul) - Data/Business Analyst

The idea of the project was to divide the workload between relevant memebers in order to have an efficient timeline for executing the project. Moreover, making use of each member's area of expertise helped in obtaining conducive insights and driving the project.

![Gantt Chart](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/Python%20Project%20-%20Gantt%20Chart.jpg)

## Data Preparation
Preparing the data for analytics is an iterative and time consuming process that can be challenging. Although all members of our team were well aware about the obstacles to come, the gameplan was to have the most experienced member lead the way for each sub-task during the course of the project, as stated in the 'Project Schedule' section. This also gave every individual the opportunity to lead one task while demonstrating the best way to go about it.

To make it easy for a reader to follow our process, we made a flowchart! After all "Seeing is believing" (in our case - "Seeing is understanding").

![Python Project Flow](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/Python%20Project%20Flow.png)

Links to all our  data files are given below:
* [Cleaned_Data_dv_2.csv](data/Cleaned_Data_dv_2.csv) The final dataset generated for this project from all sources in deliverable-2.
* [masterlist_final.csv](data/masterlist_final.csv) The final dataset generated for this project in deliverable-1.
* [ApartmentFinder_scraper.py](code/ApartmentFinder_scraper.py) Python file used to scrape data from *ApartmentFinder.com*
* [ApartmentFinder_Cleaning.py](code/ApartmentFinder_Cleaning.py) Python file used to clean, consolidate, and transform the data from *ApartmentFinder.com*
* [IndividualListings_Scrape.py](code/IndividualListings_Scrape.py) Python file used to scrape data from Individual Listings
* [IndividualListings_Cleaning.py](code/IndividualListings_Cleaning.py) Python file used to clean, consolidate, and transform the data from the individual houses
* [master_code.py](code/master_code.py) We will use this file to manipulate the main dataset during the second part of the project. for now, it gathers the seperate sources.


### Data Access
We scraped data from apartmentfinder.com and trulia.com using the Chrome driver, as seen below:
![Robots Blocking](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/data_access_sc.png)

A) apartmentfinder.com  -  Apartment Listings

It was difficult to obtain the individual values from each apartment complex in relation to each different room listed. There were different class names, even in the same columns. we settled on trying to obtain as much data from each seperate page as possible, then filled the rest in by manual searching and input. We were rewarded with a dataframe that included every available room type from each apartment/rental property on the first page of ApartmentFinder.com. We will continue to refine this process until we can gather the data from both pages of Stillwater properties.

The main stillwater page of apartmentfinder is pinged to return all href objects in a elements of a certian class. Those href elems are saved as links for the loop to scrape later. the loop looks at each link, finds the name, address, and a table of characteristics for the different apartment types available. (Beds, Baths, Rent, Availability) We will also add more variables such as amnenities soon. After the loop gathers these dispareate elements, iteration gathers them into a dataframe inside the loop. several checks are performed so that the dataframe correctly gathers the rows of data it can see for each apartment complex. the dataframe is then concatenated to the end of a growing frame outside the loop. The final iteration of this dataframe is printed to CSV, representing all the layouts for each refrenced page in the ApartmentFinder stillwater search results.


B) trulia.com  -  Individual Listings

While we were able to access and scrape apartmentfinder.com quite efficiently, the process was not as easy for "trulia.com" as it had bot protectors blocking the use of web scraping tools like Selenium. A quick way to identify if any website has bot protectors is to add "robots.txt" to the url (Eg: "trulia.com/robots.txt"). This gives a static webpage of all the variables that are blocked off for scraping from the pertinent website as shown below:

![Robots Blocking](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/robots_blocking.png)

As seen above, this website blocks web scraping tools from accessing variables like 'Rental Names', 'Home Values' (Rent Price) etc. We still decided to give it a shot but the website would give us the following error:

![Robot Check 1](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/robot_check1.png)

To counter this problem, we used Selinium's "Click & Hold" method but that still did not allow us through. The page simply looped through  the press and hold process (as seen in the screenshot below) and required us to re-launch a new chrome window to start fresh.

![Robot Check 2](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/robot_check2.png)

Since this was a hurdle we could not get past, we decided to manually scrape information of all 26 individual homes becasue they were important for our study.

### Data Cleaning
We had to perform certain tasks to clean special characters so that the observations could be easily used to make visualizations, which will be covered in our next deliverable. Further, we converted relevant columns into numeric datatypes!

A) Removing Special Characters

There were 4 particular columns in our scraped dataset that needed to be cleaned. They are:
1) Beds Column: The word "Bed/Beds" needed to be cleaned.
2) Baths Column: The word "Bath/Baths" needed to be cleaned.
3) Sqft Column: The word "sqft" needed to be cleaned.
4) Rent Column: The character "$" needed to be cleaned.

Before we delve into the cleaning process, lets look at the data that was scraped off the web:

![Before Cleaning The Data](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/Before_cleaning_ind_apts.png)

This does not look too pretty, does it? That's alright because Pandas and Regex were very helpful for us in eliminating these special characters. We used the following code to remove them:

![Data Cleaning Code](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/cleaning_code.png)

Notice how we made use of two of the most powerful python libraries to replace these redundant words/characters with ''. This process was followed for both datasets (Stand Alone Homes and Community Apartments). Now that this task was completed, we merely had to convert these columns to numeric datatypes.

B) Converting Columns to Numeric Datatype

The data we scraped off the website was stored as 'Object' which is a string datatype. These datatypes cannot be used for plotting visuals/graphs as they're text characters. We used simple Pandas "to_numeric" functions to convert these columns to numeric datatypes. The conversion code is:
![Code for Converting Datatype](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/numeric_conversion_code_sc.png)

As you would notice, this is a very simple process of converting the cleaned columns to numeric datatype. We printed the datatypes of those four columns and they were successfully converted!

![Converted Columns Datatype](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/dtype_columns.png)


### Data Transformation
There were two main transformation steps that were done for this dataset. First was to create a new column titled 'Cost Per Person' which is essentially the Total Rent for the stand alone houses divided by the number of beds. Second, we had to impute the missing values in columns 'Rent', 'Sqft' and 'Cost Per Person' with the mean or median of similar listings.

1) Cost Per Person Column

This was done using a simple Pandas function which is demonstrated below:

![Data Transformation](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/data_transformation.png)

2) Imputing Missing Values

The first step in the imputation process was to filter the dataset for relevant listings. For example, we see that the following listing on '1108 S Prairie Rd' has no square footage mentioned in the 'sqft' column as the website on which this listing was present did not have that information.

![Missing Value](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/missing_value_example.jpg)




In order to impute this value, we first created a filtered dataset with all listings having 3 beds and 2 baths and then visualized its histogram to check whether the data is skewed or not.

![Code For Filtering and Histogram](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/filtering_sim_listings.jpg) 


Here is how the histogram looked

![Histogram](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/sqft_3_beds_plot.jpg) 


From the histogram, we can see that the data is right-skewed. Hence, we will impute this missing value with the median of all similar listings having 3 beds and 2 baths. The code for the imputation is given below.

![Imputing](https://github.com/msis5193-pds1-2022fall/project-deliverable-2-red-hot-stilly-peppers/blob/main/assets/replacing_median.jpg) 

Similarly, all missing values were imputed after assessing the type of listing (Beds, Baths) and then imputing it with either Mean or Median depending on the skew of the data. The entire imputation code can be found here:
[Imputation Code](code/cleaning_transformation_2.py) 

### Data Reduction
There was no requirement of dropping any null values from our dataset as all the data scraped off the website was useful. The missing values were imputed which is elaborately explained in the 'Data Transformation' step above.

### Data Consolidation
In the end, we just had to combine the two datasets 'individual_homes_data.csv' and 'Apartmentfinder_final.csv' which gave us a dataset of 172 observations. We used the pandas concatenate function to do this task and a screenshot of the code is pasted below. 
![Merge Code](/assets/merge.png).

### Data Dictionary
We have 172 observations of the following variables. Any Nulls will be filled through manual data gathering
|Name |Description |Data Type |Source |Refrence |Example |
|---|---|---|---|---|---|
| Name | Name of the listing | string | https://www.apartmentfinder.com/, https://www.trulia.com/ | [Data](data/masterlist_final.csv) | The Links at Stillwater |
| Address | Address of the listing | string | https://www.apartmentfinder.com/, https://www.trulia.com/ | [Data](data/masterlist_final.csv) | 4599 N Washington St, Stillwater, OK 74075  |
| Bedrooms (Nos) | The number of bedrooms available in this apartment or rental house | integer | https://www.apartmentfinder.com/, https://www.trulia.com/ | [Data](data/masterlist_final.csv) | 1 |
| Bathrooms (Nos) | The number of bathrooms available in this apartment or rental house | integer | https://www.apartmentfinder.com/, https://www.trulia.com/ | [Data](data/masterlist_final.csv) | 1 |
| Availability | A date, or character value denoting status of apartment/property | string | https://www.apartmentfinder.com/, https://www.trulia.com/ | [Data](data/masterlist_final.csv) | Nov 1st, Not Available |
| Rent ($) | The amount of rent money due monthly ($ USD) | integer | https://www.apartmentfinder.com/, https://www.trulia.com/ | [Data](data/masterlist_final.csv) | 575 |
| Atributes | A list of strings denoting property attributes | list or string | https://www.apartmentfinder.com/, https://www.trulia.com/ | [Data](data/masterlist_final.csv) | Dishwasher,Wifi,Cable TV,Pool |
| Cost Per Person ($) | Rent/No. of Beds | integer | Transformed Variable | [Data](data/masterlist_final.csv) | 600, 466.6 |

## Conclusion and Discussion From Deliverable - 1
The biggest challenge we faced was that most apartment websites had bot blockers that did not allow us to scrape data off their websites. We had to formulate multiple workarounds to add some manual inputs into the process to get the code. Luckily, our study will ideally be significant for a while before we can figure out a better way to scrape the data off these marketplace websites. Through this project, we hope to allow the next year of incoming international students to find the best fit for their lifestyle and budget when searching for living quarters. The next deliverable of our study will delve into details of the variables to consider and prioritize for new migrating residents and tie the data preparation process to fruitful results.

## Results and Visualizations

Rent price and its relation to apartment size

![Cost vs Beds](https://user-images.githubusercontent.com/92104500/207749792-e2a6fade-c2a1-4586-834e-b06fccbc7024.png)

Price decreases as the number of beds go up but seem to hit a lower limit and cease decreasing after 3 beds. The cost per person decreases as the number of beds goes up. Students would prefer a low-cost price as they do not have an earning potential, they prefer to go with a minimal price. which also seems to be a reason for the increase in the number of beds and the decrease in the price.
 
![3D Walk Drive Cost](https://user-images.githubusercontent.com/92104500/207749885-4745ab99-d7ac-4a8b-8768-300663fc29f5.png)

No significant interaction between Cost and distance from Campus.There is no specific relationship between the variables. It is also observed  that there is no strong relationship or high reliability  amongst the variables when included in the graph.

![Amenities vs Cost](https://user-images.githubusercontent.com/92104500/207749896-d416df60-a045-46f0-b795-dac83fc99a67.png)

No significant difference between the number of amenities and the cost of the apartment. maybe it's just the quality of the advertisement. The highest number of data points can be noticed from 0-10 as the number of amenities is minimal, and there is high a preference. The visualization depicts that the study of the preference of students who prefer to opt for houses with minimal cost and minimal facilities. There seems to be an outlier in the graph which also has a possibility of being a house rather than an apartment as the amenities are high. Here we can also notice the fact that advertisements can gear up the student to opt for those apartments. Hence This graph infers to the major problem that the apartment should be rented at a reasonable price irrespective of the distance or the amenities provided. It is noticed that there is significant variability in price, hence this attributes to the fact that some advertisements that we scraped are more detailed and accurate compared to others.
