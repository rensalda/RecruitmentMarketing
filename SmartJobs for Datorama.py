import pandas as pd
import datetime as dt
import pendulum
from os import listdir
from os.path import isfile, join
start_time = dt.datetime.now()

folder = 'C:\\Users\\rensalda\\OneDrive - Publicis Groupe\\Documents\\' \
         'InternalMarketingProjectData\\Recruitment Marketing\\SmartJobs Datorama Feed\\'

files = [join(folder, f) for f in listdir(folder)
         if f.startswith("SmartJobs")
         and isfile(join(folder, f))]

# Append files
output_file = pd.DataFrame()
for input_file in files:
    df = pd.read_csv(input_file, skip_blank_lines=True)
    output_file = output_file.append(df)
output_file.reset_index(inplace=True, drop=True)
# output_file.to_csv(folder + 'SmartJobs_YTD_report_01.01-06.30.csv')


output_file.to_csv(folder + 'SmartJobs_YTD_report_01.01_2022-06.30_2022.csv')
