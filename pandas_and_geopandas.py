# -*- coding: utf-8 -*-

#What kind of data does pandas handle?
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {
    "Name": [
        "Braund, Mr. Owen Harris",
        "Allen, Mr. William Henry",
        "Bonnell, Miss. Elizabeth",
        ],
    "Age":[22, 35, 58],
    "Sex":["Male", "Male", "Female"],
    }
)
df


'''To manually store data in a table, create a DataFrame. 
When using a Python dictionary of lists, the dictionary keys will be used as column headers and the values in each list as columns of the DataFrame.

A DataFrame is a 2-dimensional data structure that can store data of different types (including characters, integers, floating point values, categorical data and more) in columns.
It is similar to a spreadsheet, a SQL table or the data.frame in R.

The table has 3 columns, each of them with a column label. The column labels are respectively Name, Age and Sex.

The column Name consists of textual data with each value a string, the column Age are numbers and the column Sex is textual data. '''

ages = pd.Series([22, 35, 58], name="Age")
ages


#max and min method to find the max and min value in the given array or list
df["Age"].min()
df["Age"].max()



df.describe()
#The describe() method provides a quick overview of the numerical data in a DataFrame.

''' REMEMBER
Import the package, aka import pandas as pd

A table of data is stored as a pandas DataFrame

Each column in a DataFrame is a Series

You can do things by applying a method to a DataFrame or Series '''






#How do I read and write tabular data?

#14 File Types You Can Import Into pandas
''' Python can work with the following file formats:

Comma-separated values (CSV)

XLSX (Microsoft Excel Open Xml Spreadsheet)

ZIP (there is full form to zip, ZIP is a type of archive file format. It supports lossless data compression)

Plain Text (txt)

JSON (JavaScript Object Notation (JSON) is a standardized format commonly used to transfer data as text that can be sent over a network.
      It's used by lots of APIs and Databases, and it's easy for both humans and machines to read.
      JSON represents objects as name/value pairs, just like a Python dictionary.)

XML (extensible markup language)

HTML (Hypertext Markup Language)

Images

Hierarchical Data Format

PDF

DOCX

MP3

MP4

SQL (Structured Query Language (SQL) is a standardized programming language 
     that is used to manage relational databases and perform various operations on the data in them.)'''



#this is the read method to the file external file  
titanic = pd.read_csv("titanic.csv")

titanic.head(5) #return top 5 rows
titanic.tail(10) #return buttoms 10 rows

#to check the datatype in pandas we use dtype
titanic.dtypes
'''The data types in this DataFrame are integers (int64), floats (float64) and strings (object).'''

#The method info() provides technical information about a DataFrame
titanic.info()

''' REMEMBER
Getting data in to pandas from many different file formats or data sources is supported by read_* functions.

Exporting data out of pandas is provided by different to_*methods.

The head/tail/info methods and the dtypes attribute are convenient for a first check. '''





#How do I select a subset of a DataFrame?
#How do I select specific columns from a DataFrame?

#To select a single column, use square brackets [] with the column name of the column of interest.
ages = titanic["Age"]

ages.head()

#Each column in a DataFrame is a Series. As a single column is selected, 
#the returned object is a pandas Series. We can verify this by checking the type of the output:
type(titanic["Age"])
#pandas.core.series.Series

''' DataFrame.shape is an attribute (remember tutorial on reading and writing, do not use parentheses for attributes)
 of a pandas Series and DataFrame containing the number of rows and columns: (nrows, ncolumns). 
 A pandas Series is 1-dimensional and only the number of rows is returned. '''
 
age_sex = titanic[["Age", "Sex"]]

age_sex.head()

''' Note

The inner square brackets define a Python list with column names, 
whereas the outer brackets are used to select the data from a pandas DataFrame as seen in the previous example. '''

#The returned data type is a pandas DataFrame:

type(titanic[["Age", "Sex"]])
#pandas.core.frame.DataFrame

titanic[["Age", "Sex"]].shape

#The selection returned a DataFrame with 891 rows and 2 columns. 
#Remember, a DataFrame is 2-dimensional with both a row and column dimension.



#How do I filter specific rows from a DataFrame?
above_35 = titanic[titanic["Age"] > 35]
above_35.head()

#To select rows based on a conditional expression, use a condition inside the selection brackets [].
#The condition inside the selection brackets titanic["Age"] > 35 checks for which rows the Age column has a value larger than 35:
titanic["Age"] > 35

#I’m interested in the Titanic passengers from cabin class 2 and 3.
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
class_23.head()

''' Similar to the conditional expression, the isin() conditional function returns a True for each row the values 
are in the provided list. To filter the rows based on such a function, use the conditional function inside the 
selection brackets []. In this case, the condition inside the selection brackets titanic["Pclass"].isin([2, 3])
 checks for which rows the Pclass column is either 2 or 3. '''
 
#The above is equivalent to filtering by rows for which the class is either 2 or 3 and combining the two statements with an | (or) operator:
class_23 = titanic[(titanic["Pclass"]==2) | (titanic["Pclass"] == 3)]

class_23.head()
''' Note

When combining multiple conditional statements, each condition must be surrounded by parentheses (). 
Moreover, you can not use or/and but need to use the or operator | and the and operator &. '''

#I want to work with passenger data for which the age is known.

age_no_na = titanic[titanic["Age"].notna()]

age_no_na.head()

#The notna() conditional function returns a True for each row the values are not an Null value.
#As such, this can be combined with the selection brackets [] to filter the data table.


#You might wonder what actually changed, as the first 5 lines are still the same values. One way to verify is to check if the shape has changed:
age_no_na.shape


#How do I select specific rows and columns from a DataFrame?

#I’m interested in the names of the passengers older than 35 years.
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

adult_names.head()

''' In this case, a subset of both rows and columns is made in one go and just using selection brackets [] is not sufficient anymore.
The loc/iloc operators are required in front of the selection brackets []. When using loc/iloc, the part before the comma is the rows you want, 
and the part after the comma is the columns you want to select. '''

''' When using the column names, row labels or a condition expression, use the loc operator in front of the selection brackets [].
For both the part before and after the comma, you can use a single label, a list of labels, a slice of labels, a conditional expression or a colon.
Using a colon specifies you want to select all rows or columns. '''

#I’m interested in rows 10 till 25 and columns 3 to 5.

titanic.iloc[9:25, 2:5]

''' REMEMBER
When selecting subsets of data, square brackets [] are used.

Inside these brackets, you can use a single column/row label, a list of column/row labels, a slice of labels, a conditional expression or a colon.

Select specific rows and/or columns using loc when using the row and column names

Select specific rows and/or columns using iloc when using the positions in the table

You can assign new values to a selection based on loc/iloc. '''





air_quality = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)

air_quality.head()

''' Note

The usage of the index_col and parse_dates parameters of the read_csv function to define the first (0th) column as 
index of the resulting DataFrame and convert the dates in the column to Timestamp objects, respectively. '''

#How to create plots in pandas?

#I want a quick visual check of the data.

air_quality.plot()

#With a DataFrame, pandas creates by default one line plot for each of the columns with numeric data.

#I want to plot only the columns of the data table with the data from Paris.

air_quality["station_paris"].plot()

#To plot a specific column, use the selection method of the subset data tutorial in combination with the plot() method. 
#Hence, the plot() method works on both Series and DataFrame.


#I want to visually compare the No2 values measured in London versus Paris.
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)

#Apart from the default line plot when using the plot function, a number of alternatives are available to plot data.
#Let’s use some standard Python to get an overview of the available plot methods:
[
    method_name
    for method_name in dir(air_quality.plot)
    if not method_name.startswith("_")
]

#One of the options is DataFrame.plot.box(), which refers to a boxplot. The box method is applicable on the air quality example data:
air_quality.plot.box()

#I want each of the columns in a separate subplot.

axs = air_quality.plot.area(figsize=(12, 4), subplots=True)

''' Separate subplots for each of the data columns are supported by the subplots argument of the plot functions.
The builtin options available in each of the pandas plot functions are worth reviewing. '''


#I want to further customize, extend or save the resulting plot.
fig, axs = plt.subplots(figsize=(12, 4))

air_quality.plot.area(ax=axs)

axs.set_ylabel("NO$_2$ concentration")

fig.savefig("no2_concentrations.png")

''' fig, axs = plt.subplots(figsize=(12, 4))        # Create an empty matplotlib Figure and Axes
air_quality.plot.area(ax=axs)                   # Use pandas to put the area plot on the prepared Figure/Axes
axs.set_ylabel("NO$_2$ concentration")          # Do any matplotlib customization you like
fig.savefig("no2_concentrations.png")           # Save the Figure/Axes using the existing matplotlib method. '''

''' REMEMBER
The .plot.* methods are applicable on both Series and DataFrames

By default, each of the columns is plotted as a different element (line, boxplot,…)

Any plot created by pandas is a Matplotlib object. '''

#How to create new columns derived from existing columns?
#I want to express the NO2  concentration of the station in London in mg/m^3
#(If we assume temperature of 25 degrees Celsius and pressure of 1013 hPa, the conversion factor is 1.882)

air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

air_quality.head()
#To create a new column, use the [] brackets with the new column name at the left side of the assignment.

''' Note

The calculation of the values is done element_wise. This means all values in the given column are multiplied by the value 1.882 at once.
You do not need to use a loop to iterate each of the rows! '''


#I want to check the ratio of the values in Paris versus Antwerp and save the result in a new column
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)


air_quality.head()

#If you need more advanced logic, you can use arbitrary Python code via apply().

#I want to rename the data columns to the corresponding station identifiers used by openAQ
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
''' The rename() function can be used for both row labels and column labels. 
Provide a dictionary with the keys the current names and the values the new names to update the corresponding names. '''

'''The mapping should not be restricted to fixed names only, but can be a mapping function as well. 
For example, converting the column names to lowercase letters can be done using a function as well:'''

air_quality_renamed = air_quality_renamed.rename(columns=str.lower)

air_quality_renamed.head()

''' REMEMBER
Create a new column by assigning the output to the DataFrame with a new column name in between the [].

Operations are element-wise, no need to loop over rows.

Use rename with a dictionary or function to rename row labels or column names. '''

#How to calculate summary statistics?
#What is the average age of the Titanic passengers?

titanic["Age"].mean()

#Different statistics are available and can be applied to columns with numerical data. 
#Operations in general exclude missing data and operate across rows by default.

#What is the median age and ticket fare price of the Titanic passengers?
titanic[["Age", "Fare"]].median()

#The statistic applied to multiple columns of a DataFrame is calculated for each numeric column.

#The aggregating statistic can be calculated for multiple columns at the same time. Remember the describe function from first tutorial?

titanic[["Age", "Fare"]].describe()

#Instead of the predefined statistics, specific combinations of aggregating statistics for given columns can be defined using the DataFrame.agg() method:
 

titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)

#Aggregating statistics grouped by category

#What is the average age for male versus female Titanic passengers?

titanic[["Sex", "Age"]].groupby("Sex").mean()

#As our interest is the average age for each gender, a subselection on these two columns is made first: titanic[["Sex", "Age"]]. 
#Next, the groupby() method is applied on the Sex column to make a group per category. The average age for each gender is calculated and returned.

#Calculating a given statistic (e.g. mean age) for each category in a column (e.g. male/female in the Sex column) is a common pattern.
#The groupby method is used to support this type of operations. More general, this fits in the more general split-apply-combine pattern:

#1)Split the data into groups

#2)Apply a function to each group independently

#3)Combine the results into a data structure

#The apply and combine steps are typically done together in pandas.

#In the previous example, we explicitly selected the 2 columns first. If not, the mean method is applied to each column containing numerical columns:

titanic.groupby("Sex").mean()

#It does not make much sense to get the average value of the Pclass. if we are only interested in the average age for each gender, 
#the selection of columns (rectangular brackets [] as usual) is supported on the grouped data as well:
titanic.groupby("Sex")["Age"].mean()

''' Note

The Pclass column contains numerical data but actually represents 3 categories (or factors) with respectively the labels ‘1’, ‘2’ and ‘3’.
Calculating statistics on these does not make much sense. Therefore, pandas provides a Categorical data type to handle this type of data. 
More information is provided in the user guide Categorical data section. '''

#What is the mean ticket fare price for each of the sex and cabin class combinations?

titanic.groupby(["Sex", "Pclass"])["Fare"].mean()

#Grouping can be done by multiple columns at the same time. Provide the column names as a list to the groupby() method.

#Count number of records by category
titanic["Pclass"].value_counts()
#The value_counts() method counts the number of records for each category in a column.

#The function is a shortcut, as it is actually a groupby operation in combination with counting of the number of records within each group:
titanic.groupby("Pclass")["Pclass"].count()

'''Note

Both size and count can be used in combination with groupby. Whereas size includes NaN values and just provides the number of rows 
(size of the table), count excludes the missing values. In the value_counts method, use the dropna argument to include or exclude the NaN values. '''

''' REMEMBER
Aggregation statistics can be calculated on entire columns or rows

groupby provides the power of the split-apply-combine pattern

value_counts is a convenient shortcut to count the number of entries in each category of a variable '''





air_quality = pd.read_csv(
    "air_quality_long.csv", index_col="date.utc", parse_dates=True
)


air_quality.head()


#How to reshape the layout of tables?

#Sort table rows
#I want to sort the Titanic data according to the age of the passengers.
titanic.sort_values(by="Age").head()

#I want to sort the Titanic data according to the cabin class and age in descending order.
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()

#With Series.sort_values(), the rows in the table are sorted according to the defined column(s). The index will follow the row order.

#Long to wide table format
#Let’s use a small subset of the air quality data set. We focus on  data and only use the first two measurements of each location 
#(i.e. the head of each group). The subset of data will be called no2_subset










