Matthew Davis
Final Project - DE101

Step 1: Initial Data Scraping
Run "main.py" according to the directions in "README.md" (./scrapper/README.md)

Step 2: Consolodation of Scraped Data
Run "processing.py" - this is a file I created that will combine all available CSV files for each data source (one for sales, one for products).
The combined CSV files will be located in ./combined_data and called "all_products.csv" and "all_sales.csv".

Step 3: Upload to the Data Warehouse
Create a table in Snowflake from each of the CSV files. Because there are only two files, manually uploading them is how I did this. Other possible methods could be to
have the CSV files written directly or transferred to the cloud, and stored in an S3 bucket or similar, and then pulled to Snowflake from there. 

The tables that I created for each file are names and derived as follows:
The first name is "all_products_raw", created from the "all_products.csv",
and the second table is "all_sales_raw", created from "all_sales.csv."

In the products table, one will have to change some of the column names - in the CSV file,
some column names have a dash ("-"). I have removed the dash and left the names otherwise unchanged. I have also set the first column, the unnamed column, to "ID."

Step 4: Transformation of Data

In Snowflake, I have created a SQL script to create tables from the raw data uploaded via CSV files. The fact table is the products table,
with dimensions including various datapoints about the products such as subtitle, category, type, and sales. This ensures normalized and useful data without extra dependencies.

The products table uses the UID as it's primary key, as each of these is a unique identified for each product. In addition to including subtitle ID, category ID, and type ID,
the products table has data unique to each row such as the title of the product, price information, and how customers have rated it (if applicable).

Each dimension table includes an ID and description for the data points. Subtitle ID and subtitle, Category ID and category, Type ID and type. The sales table includes
sales data, which can be linked to the products table via the included UID of the product(s) sold.

The script for the transformation of data into these tables is included in the repository as "data_warehouse_design.txt" located in the main folder of the repository.
The SQL syntax being used was written for Snowflake's SQL worksheets, so may vary slightly compared to that used when working within an RDBMS.

It can also be found here, in worksheet form, as "Project 1: Data WH Design".
https://app.snowflake.com/wapreor/afb99130/#/project-f9ldDJoHe

Step 5: Querying the Data

The final step is to query the data in order to generate some information/reports. The five questions posed are as follows:
1. Query the top 5 sales by product
2. Query the top 5 sales by category agrupation
3. Query the least 5 sales by category agrupation
4. Query the top 5 sales by title and subtitle agrupation
5. Query the top 3 products that has greatest sales by category

The queries used to generate these results are found in in the repository as "data_warehouse_design.txt" located in the main folder of the repository.
The SQL syntax being used was written for Snowflake's SQL worksheets, so may vary slightly compared to that used when working within an RDBMS.

It can also be found here, in worksheet form, as "Project 2: Query Design".
https://app.snowflake.com/wapreor/afb99130/#/project-f9ldDJoHe