from file_managment import file_managment
import pandas as pd 
import os
import random

class spreadsheet_files(file_managment):
    
    def __init__(self):
        print("My constructor")
        
        
    def read_data_frame(self,path,file_name):
        
        df = pd.DataFrame()
        type_file = file_name.split(".")
        file_path = os.path.join(path,file_name)
        
        if type_file[1] == "csv":
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
        
        columns = df.head(1)
        print(columns)
        
        return df
    
    
    def drop_empty_values(self,df):
        
        #df.dropna()
        df.dropna(inplace = True)
        print(df)
        print("removed the null values")
        
        return df
    
    def full_empty_values_all(self,df):
        
        df.fillna("Vacio", inplace = True)
        print(df)
        
        return df
    
    def full_empty_values_column(self,df,column):
        
        df[column].fillna("No email", inplace = True)
        print(df)
        return df
    
    def mean_column(self,df,column):
        
        mean_column = df[column].mean()
        print("Mean: ",mean_column)
        
        return mean_column
    
    def median_column(self, df,column):
        
        median_column = df[column].median()
        print("Median: ",median_column)
        
        return median_column
    
    def get_columns_name(self,df,column_list):
        
        df_column = df.loc[:,column_list]
        
        print(df)
        
        return df_column
        
    def drop_a_value(self,df,colum_,value_to_drop):
        
        df.drop(df.index[df[colum_] == value_to_drop], inplace = True)
        print(df)
            
        return "complete"
    
    def add_column(self,df,column_name):
        phone_list = [""]
        for num in range(1,33):
            phone_list.append(num)
        #add column
        df[column_name] = phone_list
        
        df_2 = pd.DataFrame({"Nombre":["Jorge"],"edad":[34],"Email":"generic_email@avanzado.com","telefono":[12344],"Escuela":"UDG"})
        
        df = pd.concat([df,df_2],ignore_index=True)
        
        df.to_csv(os.environ['PATH_PROJECT'] + "/" + "dataframe_testing.csv")
        
    

if __name__ == "__main__":
    obj = spreadsheet_files()
    path = os.environ['PATH_PROJECT']+ "/" + "input_files/"
    file_name = "informacion_alumnos_2.xlsx"
    column_ = "edad"
    df = obj.read_data_frame(path,file_name)
    #obj.drop_empty_values(df)
    #obj.full_empty_values_all(df)
    #obj.full_empty_values_column(df,column_)
    #obj.mean_column(df,column_)
    #obj.drop_a_value(df,"Nombre","Damian Amaury")
    #obj.median_column(df,column_)
    #obj.get_columns_name(df,["edad",'Email'])
    obj.add_column(df,"telefono")
    
    
    
    
    
    
    
    
    
    
    
        
        
        