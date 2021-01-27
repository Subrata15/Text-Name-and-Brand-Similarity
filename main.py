import pandas as pd
import numpy as np
import re

# Import Task1 class method
from cos_funct import Task1

def filterFile(path):
    # using regex findall to detect 
    # ... if any path inputed with .xlsx or .csv extension
    try:
        if re.findall(r'xlsx', path):
            df_re = pd.read_excel(path)
            return df_re
        elif re.findall(r'csv', path):
            df_re = pd.read_csv(path)
            return df_re
    except:
        sorry = pd.DataFrame({})
        return sorry

def inputPath():
    path = input('Paste your path in here..... : ')
    return path

def process_(df,a_result):
    # WARNING : Slicing and naming based on Task1 order
    df['Close Matching'] = a_result[0]
    df['Similarity'] = a_result[1]
    df['Cosine Similarity Score'] = a_result[2]
    df_new = df.copy()
    return df_new

def main():
    # using time to know how long process
    import time
    start_time = time.time()

    # get path file and fataframe based on input order
    path_df = inputPath()
    get_file = filterFile(path_df)

    if get_file.empty:
        print('We only accept xlsx or csv file only, please try again with appropriate path')
        return 'Not OK'
    
    else:
        # get similar result with calling Task1 class in here
        get_task = Task1(df=get_file, kolom_search=get_file.columns[0], 
                    kolom_loc=get_file.columns[1]) 
        # ... Please check the index of columns in the future
        similar_ = get_task.similar()

        # process into new dataframe
        df_result = process_(get_file, similar_)
        df_result.to_excel('result/ResultReportSimilarity.xlsx', index=False) 
        # ...you can change and custom name output file in here
        print('Successfully get new file with report close match and similarity columns')
        print("--- %s minutes ---" % round((time.time() - start_time)/60, 3))
        return df_result

if __name__ == '__main__':
    main()