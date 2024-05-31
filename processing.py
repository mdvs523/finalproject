import pandas
import os # To read folder/files

#combine-csvs

#Load files in product directory to dataframe
prod_dir = os.listdir("scrapper/data/products")
print('products directories defined')

prod_df = pandas.DataFrame()
for i in prod_dir:
    i=0
    if prod_dir[i]!=None:
        filename=prod_dir[i]
        prod_temp_df = pandas.read_csv(f'scrapper/data/products/{filename}')
        prod_df=prod_df._append(prod_temp_df)
        i=i+1
    else:
        break
print(prod_df)
print('products dataframe created')

#Find files in sales directory
sale_dir=[]
for dirpath, dirnames, filenames in os.walk("scrapper/data/sales/"):
   for filename in filenames:
      if filename.endswith(".csv"):
        filepath=os.path.join(dirpath, filename)
        sale_dir.append(filepath)
print('sales directories defined')

#Load files in sales directory to dataframe
sale_df = pandas.DataFrame()
for i in sale_dir:
    i=0
    if sale_dir[i]!=None:
        path_name=sale_dir[i]
        sale_temp_df = pandas.read_csv(f'{path_name}')
        sale_df=sale_df._append(sale_temp_df)
        i=i+1
    else:
        break
print(sale_df)
print('sales dataframe created')

#export complete dataframes to CSV files
if not os.path.exists('./combined_data/'):
   os.makedirs('./combined_data/')
prod_df.to_csv('./combined_data/all_products.csv', index = False)
print('products exported to csv')
sale_df.to_csv('./combined_data/all_sales.csv', index = False)
print('sales exported to csv')