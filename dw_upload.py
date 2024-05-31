import pandas
import os # To read folder/files
from snowflake.connector import connect, SnowflakeConnection


def upload_to_snowflake(connection: SnowflakeConnection, data_frame, table_name):
  with connection.cursor() as cursor:
    query = f"INSERT INTO {table_name} (name, description, price, stock, valid_for_year) VALUES (%s, %s, %s, %s, %s)"
    data = data_frame[['name', 'description', 'price', 'stock', 'valid_for_year']].values.tolist()

    cursor.executemany(query, data)

#List files in directory
list_dir = os.listdir("practice_files")
print(list_dir)

with connect(
  account="me09945",
  user="mdvs76",
  password="hugifY79pmyh3BPWZtAV",
  database="FUNDAMENTALS_DB",
  schema="PUBLIC",
  warehouse="COMPUTE_WH",
  region="us-east-2.aws"
  ) as connection:
  
  for file_name in list_dir:
  #load file to dataframe
    df = pandas.read_csv(f'./practice_files/{file_name}')
    print(df)
    _, year = file_name.split("_")
    year = year.replace(".csv", "")
    df["valid_for_year"] = year
    print(year)
    print(df)
    upload_to_snowflake(connection, df, "products")