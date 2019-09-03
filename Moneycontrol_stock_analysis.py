import pandas as pd
import numpy as np
from pandas import read_excel
from datetime import datetime

#Global variables
i = 0
new_index = []


def parse_date(date_str):
    global i
    try:
        date_value = datetime.strptime(date_str, '%m/%d/%y').date()
        i = i+1
        return date_value 
    except ValueError:
        i = i+1
        date_value = ""
        return None

def working_capital(bs):
    #bs = balance sheet data frame
    total_current_assets = bs.loc['Total Current Assets'].values
    total_current_liabilities = bs.loc['Total Current Liabilities'].values
    working_capital_ratio = total_current_assets/total_current_liabilities
    return working_capital_ratio

def acid_test(bs):
    #bs = balance sheet data frame
    total_current_assets = bs.loc['Total Current Assets'].values
    total_current_liabilities = bs.loc['Total Current Liabilities'].values
    inventory = bs.loc['Inventories'].values
    quick_ratio = (total_current_assets-inventory)/total_current_liabilities
    return quick_ratio

def debt_to_equity(bs):
    #bs = balance sheet data frame
    current_term_debt = bs.loc['Total Current Assets'].values
    long_term_debt = bs.loc['Total Current Liabilities'].values
    total_equity = bs.loc['Equity Share Capital'].values
    debt_to_equity_ratio = (current_term_debt+long_term_debt)/total_equity
    return debt_to_equity_ratio

def read_balance_sheet_data_consolidated():
    #bsdc = balance sheet data consolidated
    bsdc = pd.read_excel(r'C:/Users/joy/Documents/Python Scripts/Projects/Web_files_downloader/Coal_India_Data.xlsx', sheet_name = "Balance_Sheet_Consolidated", header = 0, index_col=0)
    bsdc = bsdc.dropna(how='all', axis = 0)
    bsdc = bsdc.dropna(how='all', axis=1)
    working_capital_ratio = working_capital(bsdc)
    print(working_capital_ratio)
    return None


#data = pd.read_excel('C:\\Users\\joy\Documents\\Python Scripts\\Projects\\Web_files_downloader\\Coal_India_Data.xlsx', sheet_name = "Income_Statement_Consolidated", header = 0)
    
read_balance_sheet_data_consolidated()




    

def read_income_statement_data_consolidated():
    #isdc = income statement data consolidated
    isdc = pd.read_excel(r'C:\Users\joy\Documents\Python Scripts\Projects\Web_files_downloader\Coal_India_Data.xlsx', sheet_name = "Balance_Sheet_Consolidated", header = 0)
    isdc.rename(columns={'Unnamed: 0':'Line Item'}, inplace=True )
    isdc = data.dropna(how='all', axis = 0)
    isdc = data.dropna(how='all', axis='columns')
    
def read_cashflow_statement_data_consolidated():
    #cfsdc = cashflow statement data consolidated
    cfsdc = pd.read_excel(r'C:\Users\joy\Documents\Python Scripts\Projects\Web_files_downloader\Coal_India_Data.xlsx', sheet_name = "Balance_Sheet_Consolidated", header = 0)
    cfsdc.rename(columns={'Unnamed: 0':'Line Item'}, inplace=True )
    cfsdc = data.dropna(how='all', axis = 0)
    cfsdc = data.dropna(how='all', axis='columns')
    


print("x")