import requests,bs4
import pandas as pd
from companylists import latest_company_list
from getdetail import get_complete_detail
from excelcalculation import format_excel_file
import os
from tqdm import tqdm
needed_items_from_website=["Sector","Shares Outstanding","Market price","52 Weeks High - Low","120 Day Average","EPS","P/E Ratio","Book Value","PBV","Market Capitalization"]
all_data=[]
# allcompanylist=["NHPC","UPPER"]
print("Please wait while we are fetching data from website.")
allcompanylist=latest_company_list("https://www.sharesansar.com/today-share-price")
for each_company in tqdm(range(0,len(allcompanylist)),desc="Getting data from website"):
    detailed_data=get_complete_detail(allcompanylist[each_company],needed_items_from_website)
    
    all_data.append(detailed_data)
    
needed_items_from_website=["Company Name"]+needed_items_from_website
tabledata =pd.DataFrame(data=all_data,columns=needed_items_from_website)
tabledata[["52 Week High","52 Week Low"]]=tabledata["52 Weeks High - Low"].str.split("-",expand=True)
del tabledata["52 Weeks High - Low"]
tabledata[["EPS","Y&Q"]]=tabledata["EPS"].str.split(" ",expand=True)
column_df=tabledata.columns.tolist()
column_df.insert(column_df.index("EPS")+1,column_df[-1])

column_df=column_df[:-1]
# print(column_df)
tabledata =tabledata.reindex(columns=column_df)
print("Please wait while we are formatting data to excel file.")
file_name="CalculationOfGrahamNumber.xlsx"
tabledata.to_excel(file_name,index=False)
tabledata.to_csv("Detail_List_In_Csv.csv",index=False)
format_excel_file(file_name)
print("Opening excel file.")
os.startfile(os.getcwd()+"\\CalculationOfGrahamNumber.xlsx")